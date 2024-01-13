import os

from trainer import Trainer, TrainerArgs
import torch
from TTS.config.shared_configs import BaseAudioConfig
from TTS.tts.configs.shared_configs import BaseDatasetConfig, CapacitronVAEConfig
from TTS.tts.configs.tacotron2_config import Tacotron2Config
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.tacotron2 import Tacotron2
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.utils.audio import AudioProcessor

from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from TTS.utils.generic_utils import get_user_data_dir

output_path = os.path.dirname(os.path.abspath(__file__))
device = "cuda" if torch.cuda.is_available() else "cpu"

data_path = "/mnt/d/LJSpeech-1.1/LJSpeech-1.1/"
taco_model = "capacitron-t2-c50/blizzard2013--capacitron-t2-c50/"

config = XttsConfig()
model_json = taco_model + "config.json"
config.load_json(model_json)

model = Xtts.init_from_config(config)
model.load_checkpoint(
    config, checkpoint_path=taco_model + "model_file.pth"
)
model.to(device)
(gpt_cond_latent, peaker_embedding) = model.get_conditioning_latents(audio_path=["split/chunk5.wav"])
