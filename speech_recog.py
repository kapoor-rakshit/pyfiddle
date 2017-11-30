# Requirements : speech_recognition ----- pip install SpeechRecognition
#              : pyaudio to access mic ----- pip install pyaudio

import speech_recognition as sr
import webbrowser

recog=sr.Recognizer()
with sr.Microphone() as src:
	audio=recog.listen(src)

try:
	msg=recog.recognize_google(audio)
	print(msg)
	link=list(msg.split())
	webbrowser.open('www.'+link[1].lower()+'.com')

except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google STT; {0}".format(e))
except:
	print("Unknown Exception Occured")