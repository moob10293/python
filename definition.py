from PyDictionary import PyDictionary
import random
dictionary=PyDictionary()
sentence = input("enter your sentence: ")
sentence = sentence.split()
print(sentence)
for x in sentence:
    try:
        print(random.choice(list(dictionary.meaning(x).values())[0]),end="|")
        #print(list(dictionary.meaning(x).values())[0],end=" ")
    except AttributeError:
        print(f"word {x} isn't a word")