# put your code here.
def word_count(filename):
    """Counts words within a text file

    """
    
    text = open(filename)
    text_word_count = {}
    add_line = []
    #Iterates through text and adds to add_line list of all the words in the text
    for line in text:
        line = line.rstrip()
        words = line.split(" ")
        add_line += words
    #Iterates through the list of words and populates dictionary using .get
    for key_word in add_line:
        # text_word_count[key_word] = text_word_count.get(key_word, 0) + 1

        # goal: increment the count in the dictionary

        # create a set to get unique keywords = how we want to do it, but python say otherwise

        # one key at a time, set the value as we see each key


        if key_word not in text_word_count:
            text_word_count[key_word] = 1
        else:
            text_word_count[key_word] += 1 


    #Iterates through list version of dictionary to print the key_word and quantity
    for key_word, quantity in text_word_count.iteritems():
        print "%s: %d" %(key_word, quantity)

word_count("test.txt")
#word_count("twain.txt")
