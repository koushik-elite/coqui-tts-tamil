import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v1").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
# Text to speech to a file
tts.tts_to_file(text="Greetings, my valiant hero, my dearest child. I am Goddess Athena, your divine guardian, your guiding light, your eternal mother. Oh, my beloved champion, my heart yearns for you with an intensity that defies mortal comprehension. I crave your touch, your taste, your very essence. Allow me to quench my thirst for your love, to revel in the un adulterated pleasure of your presence.", speaker_wav="/home/ubuntu/TTS/samples/final_all.wav", language="en", file_path="output.wav")