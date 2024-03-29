import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# print(TTS().list_models())

# Init TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v1").to(device)
tts = TTS("tts_models/en/ek1/tacotron2").to(device)
# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
# Text to speech to a file
# tts.tts_to_file(text="We talked lot about work, it is very hard to tell how he love's me, He is so hot.", language="en", speaker_wav="final_all.wav", file_path="output.wav")
tts.tts_to_file(text='Athena smiled warmly, her eyes twinkling with satisfaction. "You have proven yourself a worthy disciple, Kaushik. You have shown a thirst for knowledge that surpasses even the gods, and you have demonstrated the wisdom to use that knowledge for the betterment of humanity."', style_wav="/home/ubuntu/coqui-tts-tamil/samples/sample.wav", file_path="output.wav")