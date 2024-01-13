from pydub import AudioSegment 
from pydub.silence import split_on_silence 
import shutil
import os
import numpy as np
import soundfile

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

srcpath = "split/"
if os.path.exists(srcpath):
    shutil.rmtree(srcpath)

os.makedirs(srcpath)

# sound_file = AudioSegment.from_wav("samples/MiscellaneousMythsTheTheogony.mp3") 
sound_file = AudioSegment.from_file("samples/1_AGodAttention_(Vocals).wav") 
audio_chunks = split_on_silence(sound_file, min_silence_len=900, silence_thresh=-50 ) 
    

for i, chunk in enumerate(audio_chunks):
    # audio_chunk = AudioSegment(data=chunk.astype("float32").tobytes(), sample_width=2, frame_rate=24000, channels=1)
    audio_chunk = chunk.set_frame_rate(24000)
    audio_chunk = audio_chunk.set_channels(1)
    audio_chunk = audio_chunk.set_sample_width(2)

    # silence_chunk = AudioSegment.silent(duration=500)
    # audio_chunk = silence_chunk + audio_chunk + silence_chunk
    # audio_chunk = chunk
    normalized_chunk = match_target_amplitude(audio_chunk, -20.0)
    # normalized_chunk = audio_chunk
    out_file = srcpath + "chunk{0}.wav".format(i) 
    print("exporting", out_file) 

    # data = chunk._data
    # data_array = np.frombuffer(data, dtype=np.int32) # must use int32, this data is actually in 32bit fixed signed
    # data_array = data_array.reshape(-1, 1)

    # soundfile.write(file=out_file, data=data_array, samplerate=24000, subtype='PCM_24')

    # samples = chunk.get_array_of_samples()
    # print(samples)
    # shifted = samples * (2 ** 31 - 1)   # Data ranges from -1.0 to 1.0
    # ints = shifted.astype(np.int32)
    # sound = AudioSegment(ints.tobytes(),
    #                     format='wav',   #  we don't have headers in the raw bytes
    #                     sample_width=2, #  4 bytes, so 32 bit sample
    #                     frame_rate=24000, 
    #                     channels=1)     #  mono
    # sound.export(out_file, format="wav") 

    normalized_chunk.export(out_file, format="wav") 