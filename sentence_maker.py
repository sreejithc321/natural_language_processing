'''
Random sentence Maker

A program that can predict the word that follows a given word
and to generate a random sentence of 20 words
'''

from nltk.corpus import gutenberg
from nltk import ConditionalFreqDist
from random import choice

CORPUS  = 'austen-persuasion.txt'
sentence_limit = 5
word_limit = 15

def find_word_probability(CORPUS):
    ''' Find word occurrence probabilty from the given corpus'''
    cfd = ConditionalFreqDist()
    prev_word = None
    for word in gutenberg.words(CORPUS):
        cfd[prev_word][word] += 1
        prev_word = word
    return cfd

def print_random_sentance(start_word, cfd):
    ''' Create random sentence starting with the given word '''
    for count in range(0,sentence_limit):
        word = start_word
        print '\n'
        sentence =[]
        for limit in range (0,word_limit):
            sentence.append(word)
            lwords=cfd[word].items()
            follower=choice(lwords)[0]
            word=follower
            limit+= 1
        print " ".join(sentence)    


cfd = find_word_probability(CORPUS)
word = raw_input('Enter a starting word : ')
try:
    print 'Generating ',sentence_limit, ' random sentences starting with :', word
    print_random_sentance(word,cfd)
except:
    print 'Word not found !!'
