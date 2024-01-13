import array
# from ffprobe import FFProbe
from pydub import AudioSegment
from pydub.utils import get_array_type

import os
from os import listdir
from os.path import isfile, join
from os import walk
from tqdm import tqdm
import shutil
import numpy as np

mypath = "/mnt/c/Users/Koushik/Documents/Audio Recorder/2023/12/clone3/"
srcpath = "/mnt/d/voice/"
combined = None
# dir_list = os.listdir(mypath)

   
for filenames in os.listdir(mypath):
    print(filenames)
    path_to_file = mypath + "/" + filenames
    # path_to_out = srcpath + f"/{count}.wav"

    # print(path_to_out)
    sound = AudioSegment.from_file(file=path_to_file)
    sound = sound.set_frame_rate(48000)
    # sound_samples = np.array(sound.get_array_of_samples())
    # reduced_noise = nr.reduce_noise(sound_samples, sr=sound.frame_rate)

    # reduced_sound = AudioSegment(
    #     reduced_noise.tobytes(), 
    #     frame_rate=sound.frame_rate, 
    #     sample_width=sound.sample_width, 
    #     channels=sound.channels
    # )

    reduced_sound = sound + 7
    mono_audios = reduced_sound.split_to_mono()

    # print(len(mono))
    # left = sound.split_to_mono()[0]
    # # print(left)
    # bit_depth = left.sample_width * 8
    # # print(bit_depth)
    # array_type = get_array_type(bit_depth)
    # # print(array_type)
    # numeric_array = array.array(array_type, left._data)
    # print(numeric_array)
    # mono_audios = stereo_audio.split_to_mono() 

    # Exporting/Saving the two mono 
    # audio files present at index 0(left) 
    # and index 1(right) of list returned 
    # by split_to_mono method 
    if len(mono_audios) > 0:
        if combined:
            combined = combined + mono_audios[0]
        else:
            combined = mono_audios[0]

        # mono_left = mono_audios[0].export(path_to_out, format="wav")
        # count = count + 1
    # break

if combined:
    mono_left = combined.export(srcpath + "asmr_4.wav", format="wav")
