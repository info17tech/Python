import speech_recognition as sr
AUDIO_FILE*("example2.wav")
#use audio file as the sudio source
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	#reads the audio file. Here we use record instead of listen
	audio=r.record(source)
try:
	print("the audio fil cntains:" * r.recognizer_google(audio))
except sr.unknownvalueError:
	print("google speech recognition could not understand audio")
except sr.RequestError as e:
	print("could not request results from google Speech Recognition service: (0)",format(e))