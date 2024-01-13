from pydub import AudioSegment, effects
from pydub.playback import play
from pydub.silence import split_on_silence 
import shutil
import os
import pandas as pd 

dataframe = pd.read_csv("1_AGodAttention_Vocals.tsv", sep='\t')
sound_file = AudioSegment.from_file("samples/1_AGodAttention_Vocals.wav") 

def convert_and_save(audio, output_path, target_sample_width, target_channels):
    # Load the audio file using pydub
    audio = audio.set_frame_rate(16000)

    # Normalize the audio
    audio = effects.normalize(audio)

    # Convert to mono if not already
    if audio.channels > 1:
        audio = audio.set_channels(1)

    # Change sample width if needed
    if audio.sample_width != target_sample_width:
        audio = audio.set_sample_width(target_sample_width)

    # Export the modified audio as a new WAV file
    audio.export(output_path, format="wav")


# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

srcpath = "split/"
if os.path.exists(srcpath):
    shutil.rmtree(srcpath)

os.makedirs(srcpath)

# Set the target sample width (1 for 8-bit, 2 for 16-bit, etc.)
target_sample_width = 2

# Set the target number of channels (1 for mono, 2 for stereo)
target_channels = 1

final_audio = None
transcript_text = " "
count = 0
combined_data = []

for index, row in dataframe.iterrows():
    x = row["start"]
    y = row["end"]
    # print(row["text"])
    chunk = sound_file[x : y]
    out_file = srcpath + "chunk{0}.wav".format(count) 

    convert_and_save(chunk, out_file, target_sample_width, target_channels)
    combined_data.append([out_file, row["text"]])
    count += 1
    

pd.DataFrame(combined_data, columns=["file", "text"]).to_csv("train_transcript.csv", index=False)