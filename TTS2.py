#pip install gtts

from gtts import gTTS
import os

fh=open("test.txt", "r")
t=fh.read().replace("\n", " ")


language = 'en'

output=gTTS(text=t, lang=language, slow=False)

output.save("test-output.mp3")
fh.close()
os.system("start test-output.mp3")