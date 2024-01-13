from pydub import AudioSegment 
from pydub.silence import split_on_silence 
import shutil
import os
import pandas as pd 

dataframe = pd.read_csv("transcript.csv")

final_audio = None
transcript_text = " "
for index, row in dataframe.iterrows():
    # print(row["file"])
    sound_file = AudioSegment.from_wav(row["file"])
    transcript_text = transcript_text + " " + row["text"]
    if final_audio:
        final_audio = final_audio.append(sound_file)
    else:
        final_audio = sound_file

final_audio = final_audio.set_frame_rate(24000)
final_audio.export("final_audio.wav", format="wav") 
print(transcript_text)