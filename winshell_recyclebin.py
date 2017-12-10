#Requirements ---  pip install pypiwin32
#                  pip install winshell

import winshell
import os

try:
	winshell.recycle_bin().empty(confirm=True,show_progress=True,sound=True)     #empty Recycle Bin
	
	filepath = os.path.abspath("test.txt")
	with open(filepath,"w") as f:
		f.write("testfile1")

	winshell.delete_file(filepath)                                               #delete a file

	print(*winshell.recycle_bin().versions(filepath),sep="\n")                   #versions of file in recycle bin

	winshell.undelete(filepath)                                                  #recovers the latest recycled version

except Exception as e:
	print(str(e))