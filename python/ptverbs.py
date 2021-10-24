import pickle
from english_words import english_words_set
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import random

words = list(english_words_set)
with open("ptverbsdictionary.pickle","rb") as f:
    ptverbs = pickle.load(f)
for x in range(1000):
    word = random.choice(words)
    while not "VBD" == pos_tag(word_tokenize(word))[0][1]:
        word = random.choice(words)
    if word not in ptverbs.keys():
        ptverbs[word] = 1
    else:
        ptverbs[word] += 1
print(ptverbs)
with open("ptverbsdictionary.pickle","wb") as f:
    pickle.dump(ptverbs, f)