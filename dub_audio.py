from pydub import AudioSegment, effects

def convert_and_save(input_path, output_path, target_sample_width, target_channels):
    # Load the audio file using pydub
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(24000)

    audio = audio + 10
    
    audio = effects.normalize(audio)

    # Convert to mono if not already
    if audio.channels > 1:
        audio = audio.set_channels(1)

    

    # Change sample width if needed
    if audio.sample_width != target_sample_width:
        audio = audio.set_sample_width(target_sample_width)

    # Export the modified audio as a new WAV file
    audio.export(output_path, format="wav")

# Example usage
input_wav_file = "samples/goddess_german_5.mp3"
output_wav_file = "output_audio.wav"

# Set the target sample width (1 for 8-bit, 2 for 16-bit, etc.)
target_sample_width = 2

# Set the target number of channels (1 for mono, 2 for stereo)
target_channels = 1

convert_and_save(input_wav_file, output_wav_file, target_sample_width, target_channels)