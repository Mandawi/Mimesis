import nltk 
from nltk.corpus import wordnet 

usr = input("Type your sentence\n")
pick = input("Do you want reversal [r] or variations [v] ?\n")

def filterNonWords(word):
    non_words = ["are", "am", "is", "her", "his", "your", "I", "we","she","he","its",".",","]

    if(word in non_words):
        return False
    else:
        return True

usr=usr.replace(".","")
usr=usr.replace(",","")

filteredUsr = list(filter(filterNonWords, usr.split()))


if pick=="r":
    for word in filteredUsr:
        synonyms = [] 
        antonyms = [] 
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas(): 
                synonyms.append(l.name()) 
                if l.antonyms(): 
                    antonyms.append(l.antonyms()[0].name()) 
        for ant in set(antonyms):
            usr=usr.replace(word,ant)
    print("No,",usr)

elif pick=="v":
    variations=[]
    variations.append(usr)
    i=0
    for word in filteredUsr:
        synonyms = [] 
        antonyms = [] 
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas(): 
                synonyms.append(l.name()) 
                if l.antonyms(): 
                    antonyms.append(l.antonyms()[0].name()) 
        g=i
        for sin in set(synonyms):
            variations.append(variations[i].replace(word,sin))
            g+=1
        i=g
    for sentence in variations:
        print(sentence)

