dim speechobject
 set speechobject=createobject("sapi.spvoice")
 message=inputbox("Content - What shall I say, your Geekness?","Title - I speak for you.")     
 speechobject.speak "You Typed " + message