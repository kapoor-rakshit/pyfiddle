# Windows toast message
# Requirments : win10toast lib ----- pip install win10toast

from win10toast import ToastNotifier
toaster = ToastNotifier()

toaster.show_toast(
	"Title\n   New  Title",
	"Content\n New data is here",
	duration=10,
	icon_path='msg.ico')    #only ICO format files are supported

toaster.show_toast("New Toast","After first")