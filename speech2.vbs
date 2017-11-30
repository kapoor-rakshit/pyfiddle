dim speechobject
 set speechobject=createobject("sapi.spvoice")
 message=inputbox("What shall I say, your Geekness?","I speak for you.")
 speechobject.speak "You Typed "+message