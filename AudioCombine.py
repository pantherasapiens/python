from pydub import AudioSegment

# Load existing audio files
audio1 = AudioSegment.from_file("existing_audio1.mp3")
audio2 = AudioSegment.from_file("existing_audio2.mp3")

# Combine them
combined_audio = audio1 + audio2

# Export the combined audio to a new file
combined_audio.export("combined_audio.mp3", format="mp3")
