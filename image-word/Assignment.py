import nltk
from nltk.corpus import stopwords
from collections import Counter

#nltk.download('stopwords')
#nltk.download('punkt')

#read txt file 
with open("paragraphs.txt", 'r') as par:
    text = par.read()

stop_words = set(stopwords.words('english'))

#print(stop_words)

from nltk.tokenize import word_tokenize ,sent_tokenize
tokenize_words = word_tokenize(text)

tokenize_words_without_stop_words =[]
for word in tokenize_words:
    if word.lower() not in stop_words:
        tokenize_words_without_stop_words.append(word)

#print(tokenize_words_without_stop_words)

word_freq = Counter(tokenize_words_without_stop_words)

for word , freq in word_freq.most_common():
    print("f {} : {}".format(word , freq))
