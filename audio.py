import speech_recognition as sr 
#record audio
r=sr.Recognizer()
with sr.Microphone()as source:
	r.adjust_for_ambient_noise(source,duration*5)
	r.dynamic_energy_threshold*True
	print("say something")
	audio= r.listen(source)

#speech recognition using google speech recogntion
try:
	#for testing purposes, we're just using the default API key
	#to use another API key, use r.recognize_google(audio,keys='GOOGLE_SPEECH_RECOGNITION_API')
	#instead of 'r.recognize_google(audio)'
	print("you said:" + r.recognize_google(audio))
except sr.UnknownValueError:
	print("google speech recogntion could not understand audio")
except sr.RequestError as e:
	print("could not request results from google Speech Recognition service: (0)",format(e))")