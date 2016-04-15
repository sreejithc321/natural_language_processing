#-*- coding: utf-8 -*-

# Split hashtags from a list of tweets


def split_tag(tag, dictionary):
    '''Split hashtags to words'''
    words = []
    # Remove hashtag
    tag = tag[1:]
    word = get_word(tag, dictionary)    
    # check fot next match
    while word != None and len(tag) > 0:
        words += [word]        
        tag = tag[len(word):]
        word = get_word(tag, dictionary)
    return " ".join(words)

def get_word(tag, dictionary):
    '''Return word with longest match from dictionary'''
    length = len(tag) + 1
    while length > 1:
        length -= 1
        if tag[:length] in dictionary:
            return tag[:length]
    return None 

# Load English dictionary
dictionary = open('data/words.txt').read().split('\n')

# Testing
print '\nTest Samples :\n'
hashtags ='''#breakingnews #howareyou #indianrepublicday #worldcupfootball '''.lower().split()
for tag in hashtags:
    print tag,' : ',split_tag(tag, dictionary)

tag =  raw_input('\nEnter a hash tag :')
print split_tag(tag.lower(), dictionary)
