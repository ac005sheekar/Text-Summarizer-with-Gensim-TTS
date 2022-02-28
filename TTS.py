#pip install gtts

from gtts import gTTS
import os

t="I love Bangladesh. I love Bangladesh."

language = 'en'

output=gTTS(text=t, lang=language, slow=False)

output.save("output.mp3")