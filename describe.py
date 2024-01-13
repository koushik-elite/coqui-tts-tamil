# import required library
from pydub import AudioSegment 
 
# import the audio file
wav_file = AudioSegment.from_file(file="output_audio.wav", format="wav") 
 
# data type for the file
print("data type for the file ", type(wav_file)) 
 
#  To find frame rate of song/file
print("frame rate of song/file ", wav_file.frame_rate)   
 
# To know about channels of file
print("channels of file ", wav_file.channels) 
# OUTPUT: 1
 
# Find the number of bytes per sample 
print("number of bytes per sample ", wav_file.sample_width ) 
# OUTPUT : 2
 
 
# Find Maximum amplitude 
print("Maximum amplitude ", wav_file.max)
# OUTPUT 17106
 
# To know length of audio file
print("length of audio file ",len(wav_file))
# OUTPUT 60000 
 
'''
We can change the attributes of file by 
changeed_audio_segment = audio_segment.set_ATTRIBUTENAME(x) 
'''
# wav_file_new = wav_file.set_frame_rate(50) 
# print(wav_file_new.frame_rate)