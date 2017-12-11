#Reference : https://docs.python.org/3/library/ctypes.html

import ctypes

try:
	ctypes.windll.user32.LockWorkStation()                #lock device
	
except Exception as e:
	print(str(e))