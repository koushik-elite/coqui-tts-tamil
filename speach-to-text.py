import torch
import zipfile
import torchaudio
from glob import glob
import pandas as pd 


device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
# device = torch.device('cpu')  # gpu also works, but our models are fast enough for CPU

model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_stt',
                                       language='en', # also available 'de', 'es'
                                       device=device)
(read_batch, split_into_batches,
 read_audio, prepare_model_input) = utils  # see function signature for details

# download a single file, any format compatible with TorchAudio (soundfile backend)
# torch.hub.download_url_to_file('https://opus-codec.org/static/examples/samples/speech_orig.wav',
#                                dst ='speech_orig.wav', progress=True)

batch_num  = 5
test_files = [f"split/chunk{i}.wav" for i in range(67)] 
# test_files = glob('split/chunk14.wav')
batches = split_into_batches(test_files, batch_size=batch_num)
print(batches)
batch_count = 0
data = []
for i in range(len(batches)):
    input = prepare_model_input(read_batch(batches[i]), device=device)
    output = model(input)
    # print("output-------------")
    # out_str = ""
    for example in output:
        # out_str = out_str  + decoder(example.cpu())
        # print(test_files[batch_count], decoder(example.cpu()))
        data.append([test_files[batch_count], decoder(example.cpu())])
        batch_count += 1

print(data)
# dataframe = pd.DataFrame(data, columns=["file", "text"])
# dataframe.to_csv("transcript.csv", index=False)