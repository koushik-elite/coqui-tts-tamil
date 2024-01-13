from pathlib import Path

from TTS.utils.synthesizer import Synthesizer
from TTS.utils.manage import ModelManager
import uuid

# transcript = "oh do you forgive me mortal i did not mean to wake you i felt for my chariot you see and you'd like to see the injury very well sprained well i thank you for the medical prognosis mortal and why do i keep callingme mortal because you are am i not as well silly i'm a thenina god of wisdom craft and war and you a lovely name butoh oh my i didn't expect you to be able to lift me you're quite strong for aimmortal oh farmer i see i see we're going into a little home while we well it's not my ideal seduction scenario but you know i don't think i've ever met immoral that was so un impacted by my divine splendor do you already have the spouse no a lover no well do you perhaps act as a concubine for a god do you belonged to one of my brother's and sisters you belong to no one interesting you don't need to drop my ankle so tightly love it'll heal just fine in no time food a water i appreciate your kindness mortal but really i'm quite allright i feel just awful if i didn't repeg you somehow don't need a repayment you are challenge my friend fortunately i do love a good challenge you seem like you might need your shoulders rotator perhaps i could ease my hands to feisty you're getting the all worked up mortal and i do get to be travel omem it by hanging around you randy little things for too long why do you think there's so many demi gods Hmm oh not for me no i'm not much of the child person they make things so complicated am i trying to seduce you i love no i am expertly succeeding to seduce you oh ordering me to get out very well but will you humor me with one more little quark of mine you see i do love betting so i say we've bit coin to decide to decide what well if it heads in your mindine my concubine or petter whatever term me prefer and if its tales then you have a gogot at your disposal for all eternity my beautiful friends come now if you really believe that i am an ordinary woman how could i force you to be ine if i win you have to me about like i was a care and if i lose well free labor what do you have to lose my beauty go on roll the odds brave mortal come let me till your head up just a touch so i can see those e lovely now are you prepared then let us see what the sisters of fates todecsi had did this well then my newmortal pet allow me to carry you over the threshold like one of your little princesses you all ado so much here we are homes sweet home Hmm mortal you're holding tightly to me already do you not want me to court you first not that i mind i have all the time in the world for pleasure who am i love i already told you i'm athena the godess of war and you my sweet belong to me now i told you mortal if i guess the coin toss correctly you would be mine if you did i would be at your disposal the coin was heads oh i do love them feisty accusing me of cheating well you're not necessarily wrong between you and i i was going to take you anyways welcome home my new little toy i'll do my best not to break you"
# refaudio = "final_audio.wav"

transcript = "and why do i keep callingme mortal because you are"
refaudio = "split/chunk5.wav"

# transcript = "she thought it was the middle of the night when she was awakened by such dreadful sounds that she jumped out of bed in an instant."
# refaudio = "samples/BLZ80762.wav"

text = "Greetings, My valiant champion, My dearest child"



text = transcript[0:200]

model = "capacitron-t2-c50/blizzard2013--capacitron-t2-c50/"
VOCODER_PATH = "capacitron-t2-c50/vocoder_models--en--blizzard2013--hifigan_v2/"

def synthesize_wrapper(model, text, reference_info):
    # load models
    model_path = model + "model_file.pth"
    config_path = model + "config.json"
    synthesizer = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
        tts_speakers_file=None,
        tts_languages_file=None,
        vocoder_checkpoint=VOCODER_PATH + "model_file.pth",
        vocoder_config=VOCODER_PATH + "config.json",
        encoder_checkpoint=None,
        encoder_config=None,
        use_cuda=False,
    )

    # RUN THE SYNTHESIS
    print(" > Text: {}".format(text))

    # kick it
    wav = synthesizer.tts(
        text,
        None,
        None,
        style_wav=reference_info["reference_wav"], 
        style_text=reference_info["reference_text"]
        )

    out_path = "{}_{}_{}_output.wav".format(
        "posterior" if reference_info["reference_wav"] is not None else "prior", 
        "C=50" if "c50" in model_path else "c150",
        str(uuid.uuid4())[:5]
        )

    # save the results
    print(" > Saving output to {}".format(out_path))
    synthesizer.save_wav(wav, out_path)
    # display(Audio(out_path))
    return out_path

reference_info={
    "reference_wav" : refaudio, 
    "reference_text" : transcript
}

synthesize_wrapper(model, text, reference_info)

# synthesizer = Synthesizer(model_path, config_path)

# wav = synthesizer.tts(text)
# synthesizer.save_wav(wav, "robot.wav")

