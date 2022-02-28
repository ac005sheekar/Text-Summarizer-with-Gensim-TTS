#Use gensim 3.8.3
#pip install gensim==3.8.3
#pip install gensim_sum_ext

text="Employees don’t need to be friends with their boss but they need to have a relationship. " \
     "The boss is too much of an integral part of their daily lives at work for an uncomfortable relationship. " \
     "The boss provides direction and feedback, spends time in one-to-one meetings, and connects the employee to the larger organization. " \
     "To have a toxic relationship with the person an employee reports to undermines the employee’s engagement, confidence, and commitment. " \
     "According to many sources, a bad boss is also the number one reason why employees quit their job. " \
     "Here's how to get along with your boss."

#print(text)

from gensim.summarization import summarize
from gensim.summarization import keywords

from gtts import gTTS
import os

t = summarize(text, word_count=10)

print("Summerized text is: \n" + t)
print("\n\n\n\n")

print("Keywords are:")
print(keywords(text))


language = 'en'

output=gTTS(text=t, lang=language, slow=False)
output.save("boss.mp3")

os.system("start boss.mp3")
