
#This pyscript creates a vbscript file and then open it.

import os

content='''dim speechobject
 set speechobject=createobject("sapi.spvoice")
 message=inputbox("What shall I say, your Geekness?","I speak for you.")
 speechobject.speak "You Typed "+message'''

say=open('speech2.vbs','w+')       # create vbs file
say.write(content)
say.close()
text_file='speech2.vbs'
os.startfile(text_file)           