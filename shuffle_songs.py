#Requirements : tinytag lib for reading music meta data of MP3, OGG, FLAC and Wave files with python
#             ---- pip install tinytag
#Reference    : https://pypi.python.org/pypi/tinytag/0.9.3

import os
import random
import time
from tinytag import TinyTag as tg

dirpath = os.path.abspath("----your songs dir path----")            #songs dir

songs=[]
for i in os.listdir(dirpath):
	songs.append("----your songs dir path----"+i)

l=len(songs)

st=set()

while True:
	initsize=len(st)
	fl=random.choice(songs)
	st.add(fl)
	aftersize=len(st)

	if initsize!=aftersize:
		os.startfile(fl)
		msg = fl.split('\\')
		print("Playing ",msg[5])                                         #msg[---vary acc to path args---]

	if aftersize==l:
		break
	else:
		tag = tg.get(fl)
		time.sleep(tag.duration)                                              #get info about file using tinytag lib
		continue