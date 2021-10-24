from english_words import english_words_set
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import random

words = list(english_words_set)
listofwords =["JJ", "NN","VBD","NN"]
sentence = []
#greedybugsee
for x in listofwords:
    word = random.choice(words)
    while not x == pos_tag(word_tokenize(word))[0][1]:
        word = random.choice(words)
    sentence.append(word)
sentence = ["the"]+sentence
for x in sentence:
    print(x,end=" ")
"""
# import required modules
  
# taking input text as India
text = "India"y54
ans = nltk.pos_tag()
  
# ans returns a list of tuple
val = ans[0][1]
  
# checking if it is a noun or not
if(val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
    print(text, " is a noun.")
else:
    print(text, " is not a noun.")"""