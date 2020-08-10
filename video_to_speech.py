import speech_recognition as sr
import moviepy.editor as me


try:
	video_clip = me.VideoFileClip(r"test.mp4")

	# Extracting audio from video
	video_clip.audio.write_audiofile(r"converted.wav")

	# Defining the recognizer
	recognizer =  sr.Recognizer()
	# importing audio file for recognition
	audio_clip = sr.AudioFile("converted.wav")

	# converting speech to text.
	with audio_clip as source:
		audio_file = recognizer.record(source)

	result = recognizer.recognize_google(audio_file)


	with open('recognized.txt', 'w') as file:
		file.write(result)
		print("Speech to text conversion successfull.")

except Exception as e:
	print("Attempt failed -- ", e)
