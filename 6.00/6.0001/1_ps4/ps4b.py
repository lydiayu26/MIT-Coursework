# Problem Set 4B
# Name: Lydia Yu
# Collaborators: Aditya Mehrotra
# Time Spent: 8:00
# Late Days Used: 0

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = input_text
        self.valid_words = load_words('words.txt')

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        words = self.valid_words
        return words

    def make_shift_dicts(self, input_shifts):
        '''
        Creates a list of dictionaries; each dictionary can be used to apply a
        cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. By shifted down, we mean
        that if 'a' is shifted down by 2, the result is 'c.'

        The dictionary should have 52 keys of all the uppercase letters and
        all the lowercase letters only.

        input_shifts (list of integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a list of dictionaries mapping letter (string) to
                 another letter (string).
        '''
        dictlist = []
        
        for num in input_shifts:
            #each list item is a dictionary that has key as original letter and value as letter after shift
            lowerletterdict = {}
            for i in range(len(string.ascii_lowercase)):
                #if the index of the letter + amount it is shifted by >25, subtract 25 so letters go back to beginning
                if i + num > 25:
                    lowerletterdict[string.ascii_lowercase[i]] = string.ascii_lowercase[i+num-25]
                else:
                    lowerletterdict[string.ascii_lowercase[i]] = string.ascii_lowercase[i+num]
            
            upperletterdict = {}
            for j in range(len(string.ascii_uppercase)):
                if i + num > 25:
                    upperletterdict[string.ascii_uppercase[i]] = string.ascii_uppercase[i+num-25]
                else:
                    upperletterdict[string.ascii_uppercase[i]] = string.ascii_uppercase[i+num]
               
            #combines lower and upper letter dicts to one dict and adds that to dictlist
            l = lowerletterdict
            letterdict = l.update(upperletterdict) 
            dictlist.append(letterdict)
            
            

    def apply_shifts(self, shift_dicts):
        '''
        Applies the Caesar Cipher to self.message_text with letter shifts
        specified in shift_dicts. Creates a new string that is self.message_text,
        shifted down the alphabet by some number of characters, determined by
        the shift value that shift_dicts was built with.

        shift_dicts: list of dictionaries; each dictionary with 52 keys, mapping
            lowercase and uppercase letters to their new letters
            (as built by make_shift_dicts)

        Returns: the message text (string) with every letter shifted using the
            input shift_dicts

        '''
        chars = list(self.get_message_text())
        
        #checks to make sure chars[i] is a letter, then changes chars[i] to shifted letter
        for i in range(len(chars)):
            if chars[i].isalpha():
                if i%2 == 0:
                    chars[i] = shift_dicts[0].get(chars[i])
                else:
                    chars[i] = shift_dicts[1].get(chars[i])
                    
        return ''.join(chars)
                
            


class PlaintextMessage(Message):
    def __init__(self, input_text, input_shifts):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        input_shifts (list of integers): the list of shifts associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shifts (list of integers, determined by input shifts)
            self.encryption_dicts (list of dictionaries, built using shifts)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        Message.__init__(self, input_text)
        self.shifts = input_shifts
        self.encryption_dicts = Message.make_shift_dicts(self, input_shifts)
        shift_dicts = self.encryption_dicts
        self.encrypted_message_text = Message.apply_shifts(self, shift_dicts)

    def get_shifts(self):
        '''
        Used to safely access self.shifts outside of the class

        Returns: self.shifts
        '''
        return self.shifts

    def get_encryption_dicts(self):
        '''
        Used to safely access a copy self.encryption_dicts outside of the class

        Returns: a COPY of self.encryption_dicts
        '''
        dicts = self.encryption_dicts
        return dicts

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text

    def modify_shifts(self, input_shifts):
        '''
        Changes self.shifts of the PlaintextMessage, and updates any other
        attributes that are determined by the shift list.

        input_shifts (list of length 2): the new shift that should be associated with this message.
        [0 <= shift < 26]

        Returns: nothing
        '''
        self.shifts = input_shifts
        self.encryption_dicts = Message.make_shift_dicts(self, input_shifts)
        shift_dicts = self.encryption_dicts
        self.encrypted_message_text = Message.apply_shifts(self, shift_dicts)


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the message's text

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, input_text)

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible combination of shift
        values and finding the "best" one.
        We will define "best" as the list of shifts that creates the maximum number
        of valid English words when we use apply_shifts(shifts)on the message text.
        If [a, b] are the original shift values used to encrypt the message, then we
        would expect [(26 - a), (26 - b)] to be the best shift values for
        decrypting it.

        Note: if multiple lists of shifts are equally good, such that they all create
        the maximum number of valid words, you may choose any of those lists
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value list used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shifts = []
        validwords = 0
        maxvalids = 0
        
        #iterates through all possible shifts for a and b
        for a in range(26):
            for b in range(26):
                shifts = Message.make_shift_dicts(self, [a,b])
                words = Message.apply_shifts(self, shifts).split()
                #if the word in the shifted message is a valid word, add one to validwords
                for w in words:
                    if is_word(self.get_valid_words(), w):
                        validwords += 1
                #if validwords is greater than previous maxvaids value, make that the new maxvalids and set the associated shift lists and decrypted message
                if validwords > maxvalids:
                    maxvalids = validwords
                    best_shifts = [a,b]
                    decrypt = words
        
        
        return (best_shifts, decrypt)


def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (PlaintextMessage) #####

#    # This test is checking encoding a lowercase string with punctuation in it.
#    plaintext = PlaintextMessage('hello!', [2,3])
#    print('Expected Output: jhnoq!')
#    print('Actual Output:', plaintext.get_encrypted_message_text())

    #this test tests a string with nonalpha characters
    message = PlaintextMessage("cs is cool!", [1, 4])
    print("Expected output: dw jw dspp!")
    print("Actual output: " + message.get_encrypted_message_text())
    
    #tests string with upper and lowercase letters
    message = PlaintextMessage("hElLoWoRlD", [3, 5])
    print("Expected output: kJoQrBrWoI")
    print("Actual output: " + message.get_encrypted_message_text())

def test_encrypted_message():
    '''
    Write two test cases for the EncryptedMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (EncryptedMessage) #####

#   # This test is checking decoding a lowercase string with punctuation in it.
#    encrypted = EncryptedMessage('fbjim!')
#    print('Expected Output:', ([2, 3], 'hello!'))
#    print('Actual Output:', encrypted.decrypt_message())

    #decodes string with punctuation
    message = EncryptedMessage("dw jw dspp!")
    print("Expected output: cs is cool!")
    print("Actual output: " + message.decrypt_message())
    
    #decodes string with upper nad lowercase letters
    message = EncryptedMessage("kJoQrBrWoI")
    print("Expected output: hElLoWoRlD")
    print("Actual output: " + message.decrypt_message())

def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your EncryptedMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    story = get_story_string()
    encrypted = EncryptedMessage(story)
    return encrypted.decryptMessage()

if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    test_plaintext_message()
    test_encrypted_message()

    # Uncomment these lines to try running decode_story_string()
    best_shift, story = decode_story()
    print("Best shift:", best_shift)
    print("Decoded story: ", story)
    pass
