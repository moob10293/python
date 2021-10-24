from typing import Sequence
from english_words import english_words_set
import random, classes
Sentence = []
for x in range(random.randint(3,20)):
    Sentence.append(random.choice(list(english_words_set)))
for x in Sentence:
    print(x,end=" ")
print("")
changerate = classes.chance(1,100)
smthing = input("which function? ")
while smthing != "quit":
    try:
        smthing = int(smthing)
    except ValueError:
        if smthing == "regen":
            Sentence.clear()
            for x in range(random.randint(3,10)):
                Sentence.append(random.choice(list(english_words_set)))
            for x in Sentence:
                print(x.rstrip(),end=" ")
            print("")
        elif smthing == "mutate":
            mutated = Sentence.copy()
            for x in range(len(mutated)):
                if changerate.getchance():
                    mutated[x] = random.choice(list(english_words_set))
            for x in Sentence:
                print(x,end=" ")
            print("")
            smthing = input("chose? ")
            if smthing == "yes":
                Sentence = mutated
            while smthing == "recheck":
                mutated = Sentence.copy()
                for x in range(len(mutated)):
                    if changerate.getchance():
                        mutated[x] = random.choice(list(english_words_set))
                print(mutated)
                smthing = input("chose? ")
                if smthing == "yes":
                    Sentence = mutated
                    break
    else:
        changerate = classes.chance(smthing,100)
    smthing = input("which function? ")