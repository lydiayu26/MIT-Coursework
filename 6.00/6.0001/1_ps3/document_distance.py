# 6.0001 Fall 2018
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k

# Problem Set 3
# Name: Lydia Yu
# Collaborators: Aditya Mehrotra
# Time Spent: 2 hours
# Late Days Used: none 

import string

### DO NOT MODIFY THIS FUNCTION
def load_text(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    print("Loading file...")
    inFile = open(filename, 'r', encoding='ascii', errors='ignore')
    line = inFile.read()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()

### Problem 1 ###
def get_frequencies(words):
    """
    Args:
        words: either a string of words or a list of words
    Returns:
        dictionary that maps str:int where each str 
        is a word in words and the corresponding int 
        is the frequency of the word in words
    """
    #if words is a string, convert it to a list by splitting from each space
    if type(words) == str:      
        words = words.split(" ")        
    
    freq = {}     
    
    #if the word is not already in the dictionary, add it; if it's in there, increase its value
    for w in words:        
        if w not in freq:       
            freq[w] = 1
        else:
            freq[w] += 1       
            
    return freq

### Problem 2 ###
def find_bigrams(text):
    """
    Args:
        text: string
    Returns:
        list of bigrams from input text
    """
    #convert text to an array of strings
    text = text.split(" ")
    
    bigrams = []
    
    #goes through text and adds each pair of words to bigrams
    for i in range(len(text)-1):
        bigrams.append(text[i] + " " + text[i+1])
        
    return bigrams

### Problem 3 ###
def calculate_similarity(dict1, dict2):
    """
    Args:
        dict1: frequency dictionary of bigrams for one text
        dict2: frequency dictionary of bigrams for another text
    Returns:
        float, a number between 0 and 1, inclusive 
        representing how similar the texts are to each other
        
        The difference in text frequencies = DIFF sums words 
        from these three scenarios: 
        * If a word occurs in dict1 and dict2 then 
          get the difference in frequencies
        * If a word occurs only in dict1 then take the 
          frequency from dict1
        * If a word occurs only in dict2 then take the 
          frequency from dict2
         The total frequencies = ALL is calculated by summing 
         all frequencies in both dict1 and dict2. 
        Return 1-DIFF/ALL rounded to 2 decimal places
    """
    DIFF = 0
    
    #adds difference of frequencies of words to DIFF if they appear in both dict1 and dict2. if just in dict1, add that frequency
    for w in dict1:
        if w in dict2:
            DIFF += abs(dict1[w] - dict2[w])
        else:
            DIFF += dict1[w]
    
    #if the word is just in dict2 then add its frequency to DIFF        
    for i in dict2:
        if i not in dict1:
            DIFF += dict2[i]
                    
    ALL = 0
    
    #sums frequencies of all words in dict1 and dict2
    for w in dict1:
        ALL += dict1[w]
    for i in dict2:
        ALL += dict2[i]
        
    return (float(1-DIFF/ALL))

### Problem 4 ###
def get_most_frequent_words(dict1, dict2):
    """
    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) shared between the 2 texts
        
        The most frequent word is defined as the combined 
        frequency of shared words across both texts.
        If multiple words share the same highest frequency, return
        all of them in alphabetical order.
    """
    words = []
    freqs = {}
    
    for w in dict1:
        if w in dict2:
            freqs[w] = dict1[w] + dict2[w]
            
    x = 0
    #finds the word with the highest frequency in freqs
    for f in freqs:
        if freqs[f] >= x:
            x = freqs[f]
            
    #adds all words with the highest frequency to words
    for i in freqs:
        if freqs[i] == x:
            words.append(i)
            
    words.sort()
    return words
        

filename1 = "hello_world.txt"
filename2 = "hello_friends.txt"

# load texts
text1 = load_text(filename1)
text2 = load_text(filename2)

# get bigrams
bigrams1 = find_bigrams(text1)
bigrams2 = find_bigrams(text2)

# get frequency dictionaries for each text using each method
freq_dict1_word = get_frequencies(text1)
freq_dict2_word = get_frequencies(text2)
freq_dict1_bigram = get_frequencies(bigrams1)
freq_dict2_bigram = get_frequencies(bigrams2)

# get how similar the texts are
similarity_w = calculate_similarity(freq_dict1_word, freq_dict2_word)
similarity_b = calculate_similarity(freq_dict1_bigram, freq_dict2_bigram)
print("Similarity based on words: ", similarity_w)
print("Similarity based on bigrams: ", similarity_b)

# get most frequent word in both texts
most_frequent_word = get_most_frequent_words(freq_dict1_word, freq_dict2_word)
print("Most frequent shared word: ", most_frequent_word)
