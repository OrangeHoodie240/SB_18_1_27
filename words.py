def print_upper_words(words, must_start_with=None):
    """
        prints each word in list in all uppercases
        Optional must_start_with takes set of characters and will ignore any words not starting with a character in the set.
    """

    for word in words:
        if(word[0] in must_start_with):
            print(word.upper())


# should print 
#   CAT
#   GATOR
#   CAR
#   GUITAR
print_upper_words(['dog', 'cat', 'gator', 'car', 'guitar', 'engine'], must_start_with={'c', 'g'})