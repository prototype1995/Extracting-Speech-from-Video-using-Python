import speech_recognition as sr
import moviepy.editor as me

VIDEO_FILE = "test.mp4"
OUTPUT_AUDIO_FILE = "converted.wav"
OUTPUT_TEXT_FILE = "recognized.txt"

try:
	video_clip = me.VideoFileClip(r"{}".format(VIDEO_FILE))

	# Extracting audio from video
	video_clip.audio.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))

	# Defining the recognizer
	recognizer =  sr.Recognizer()
	# importing audio file for recognition
	audio_clip = sr.AudioFile("{}".format(OUTPUT_AUDIO_FILE))

	# converting speech to text.
	with audio_clip as source:
		audio_file = recognizer.record(source)
	print("Please wait ...")

	result = recognizer.recognize_google(audio_file)


	with open(OUTPUT_TEXT_FILE, 'w') as file:
		file.write(result)
		print("Speech to text conversion successfull.")

except Exception as e:
	print("Attempt failed -- ", e)
