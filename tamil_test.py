import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# print(TTS().list_models())

# Init TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v1").to(device)
tts = TTS("tts_models/en/ljspeech/glow-tts").to(device)

# tts = TTS(model_path="capacitron-t2-c50/best_model_700.pth").to(device)
# tts = TTS(model_name="TTS/TTS/tts/models/tacotron2.py", progress_bar=True).to(device)
# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
# Text to speech to a file
# tts.tts_to_file(text="We talked lot about work, it is very hard to tell how he love's me, He is so hot.", language="en", speaker_wav="final_all.wav", file_path="output.wav")
# tts = TTS("tts_models/en/blizzard2013/capacitron-t2-c50").to(device)
# tts.tts_with_vc_to_file(
#     "am I not as well silly? I'm Athena, god of wisdom craft and war and you?",
#     speaker_wav="samples/BLZ80762.wav",
#     file_path="ouptut_c50_1.wav",
# )
tts.tts_to_file(
    "am I not as well silly? I'm Athena, god of wisdom craft and war and you?",
    file_path="ouptut_c50_1.wav",
)