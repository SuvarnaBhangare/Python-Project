import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hours = int(datetime.datetime.now().hour)
	if hours>=0 and hours<12:
		speak("Good Morning!")
	elif hours>=12 and hours<18:
		speak("Good Afternoon..")
	else:
		speak("Good Evenning!")
	
	speak("Hii Mam I am Jarvis.. How May i help You")

def takeCommand():
	# it takes microphone input fron user and retirn string input
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listining...")
		r.pause_threshold = 1
	
	


if __name__ == "__main__":
	wishMe()







