#uses Windows builtin SAPI (Speech API)

#This pyscript creates a vbscript file and then open it.

import os
import win32com.client as wincl

content='''dim speechobject
 set speechobject=createobject("sapi.spvoice")
 message=inputbox("Content - What shall I say, your Geekness?","Title - I speak for you.")     
 speechobject.speak "You Typed " + message'''

say=open('speech2.vbs','w+')       # create vbs file
say.write(content)
say.close()
text_file='speech2.vbs'
os.startfile(text_file)           


#this pyscript uses Dispatch() method of wincl.client to invoke Windows SAPI

#Requirements ---  pip install pypiwin32

speakobj = wincl.Dispatch("sapi.spvoice")
speakobj.speak("Hello Sopho? how are you doing ?")
speakobj.speak('''HI Kapoors''')