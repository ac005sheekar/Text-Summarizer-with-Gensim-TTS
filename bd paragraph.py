#Use gensim 3.8.3
#pip install gensim==3.8.3
#pip install gensim_sum_ext

text="Bangladesh is a small but developing country. " \
     "It is in South Asia. " \
     "It is surrounded by India on three sides and by the Bay of Bengal in the South and by Myanmar with a few areas. " \
     "She got her independence or freedom in 1971 after a long bloody battle with Pakistan. It has a tropical monsoon climate. The country is crisscrossed by many rivers and canals. So, Bangladesh is called a riverine country. The main rivers of the country are the Padma, the Meghna, the  Jamuna, the Surma, the Teesta and the Karnafully.  Rice Jute, sugarcane, wheat and pulse are the main crops here. More than 160 million people live here. Most of the inhabitants are Muslims. There also live many Hindus, Buddhists and Christians here. The people of Bangladesh are very hospitable and friendly. All people here live in great peace and amity. Each year different festivals such as Pahela Baishakh, the Bangla Nababarsho, Happy New year’s day, Durgapuza, Buddha  Purnima, Christmas Day and so on are celebrated here with great enthusiasm and festivity. The main occupation of the people here is agriculture. Some people also earn their livelihood by fishing, farming, poultry rearing, cattle rearing, labouring, business etc.  Bangladesh is blessed with stunning natural beauties. She has some attractive places like Cox’s Bazar sea beach – the largest beach in the world, Kuakata sea beach, Moynamoti, Bandarban forest, Rangamati etc. She also belongs to some world heritage sites. They are Sundarbans- the biggest mangrove forest, Paharpur Buddha Bihar and Shat Gambuj Mosque. All the places have become attractive tourist spots. I really feel proud of my country."

#print(text)

from gensim.summarization import summarize
from gensim.summarization import keywords

from gtts import gTTS
import os

t = summarize(text, word_count=50)

print("Summerized text is: \n" + t)
print("\n\n\n\n")

print("Keywords are:")
print(keywords(text))


language = 'en'

output=gTTS(text=t, lang=language, slow=False)
output.save("bd.mp3")

os.system("start bd.mp3")
