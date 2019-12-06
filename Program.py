import re
import spacy
from spacy import displacy
from collections import Counter
import random
import difflib
import nltk


nlp = spacy.load('en_core_web_sm')
answer = 'Yes'

while True:
    sentence = input("Put in your sentence: ")
    words = {}
    
    wordtype_list = []
    gibberish = 0

    doc1 = nlp(sentence)

    sentence = sentence.lower()
    sen_words = nltk.word_tokenize(sentence)

    wordtype_list = [] #this is the list of scientific words identified

    words = [] #the words from the scientific text file but they have \n at the end of all of them
    with open('Scientificwords.txt') as f:
        for i in f:
            words.append(i)

    word_set = [] #this is the wordset with all the \n removed
    for i in words:
        word_set.append(re.sub('\\n', '', i))


    if len(sentence) == 0: #Sees if the question is long enough
        print('There is not enough user input')
        exit()

    else:
        wordlist = open('wordlist.txt').read().splitlines()

        for spelling in sen_words:
            result = difflib.get_close_matches(spelling, wordlist, n=5, cutoff=0.8)
            if result:
               pass
            else:
                gibberish+=1

        if gibberish >=2:
            print("Your question has words that don't make sense.") #if there's misspelled words

        else: 
            verb_check=0

            tagged = nltk.pos_tag(sen_words)
            finaltext1 = [word for (word, pos) in tagged if pos in ('VBN', 'VBD','VB','VBZ','VBG','VBP')]

            verb_check = len(finaltext1) 

            if verb_check <1:
                print('I am sorry, but your question does not sound complete.') #if it's not a complete sentence

            else: #checking if ther words in the sentence match with the words in the text file
                for word in word_set:
                    for token in doc1:
                        if token.text == word:
                            wordtype_list.append(token)

                print(wordtype_list)
                if len(wordtype_list) > 0:
                    print("Your question is scientific!")
                else:
                    print("Your question is not scientific")


    answer = input("Would you like to go again? (Enter Yes or No): ")
    while answer != 'No' and answer != 'Yes':
        answer = input("Oops! Could you please put 'Yes' or 'No'?: ")
    if answer == 'No':
        exit()





    #for ent in doc1.ents:
        #words[ent.text] = ent.label_

    #for key in words:
        #if words[key] == 'NORP':
            #print("Your question seems to be a political one!")

    #print("It appears your question isn't political")