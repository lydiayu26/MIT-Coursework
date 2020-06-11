import os
import document_distance as ds
import unittest
import string
    
# Test shell
class TestWordFrequency(unittest.TestCase):
     def load_text(self, filename):
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
    
     def test_frequency_hello_world(self):
         text = self.load_text("hello_world.txt")
         result = ds.get_frequencies(text)
         expected = {"hello":2, "world":1}
         self.assertDictEqual(result, expected)
    
     def test_frequency_1a(self):
         text = self.load_text("test1a.txt")
         result = ds.get_frequencies(text)
         expected = {'from': 2, 'time': 2, 'to': 5, 'this': 1, 'submerged': 1, 'or': 1, 'latent': 1, 'theater': 1, 'in': 3, 'becomes': 1, 'almost': 1, 'overt': 1, 'it': 2, 'is': 3, 'close': 1, 'the': 10, 'surface': 2, 'hamlets': 1, 'pretense': 1, 'of': 7, 'madness': 1, 'antic': 1, 'disposition': 1, 'he': 3, 'puts': 1, 'on': 1, 'protect': 1, 'himself': 2, 'and': 5, 'prevent': 1, 'his': 3, 'antagonists': 1, 'plucking': 1, 'out': 2, 'heart': 1, 'mystery': 1, 'even': 1, 'closer': 1, 'when': 2, 'hamlet': 2, 'enters': 1, 'mothers': 1, 'room': 1, 'holds': 1, 'up': 1, 'side': 2, 'by': 2, 'pictures': 1, 'two': 1, 'kings': 1, 'old': 1, 'claudius': 1, 'proceeds': 1, 'describe': 1, 'for': 3, 'her': 1, 'true': 1, 'nature': 1, 'choice': 1, 'she': 1, 'has': 1, 'made': 1, 'presenting': 1, 'truth': 1, 'means': 1, 'a': 1, 'show': 1, 'similarly': 1, 'leaps': 1, 'into': 1, 'open': 1, 'grave': 1, 'at': 1, 'ophelias': 1, 'funeral': 1, 'ranting': 1, 'high': 1, 'heroic': 1, 'terms': 1, 'acting': 1, 'laertes': 1, 'perhaps': 1, 'as': 1, 'well': 1, 'folly': 1, 'excessive': 1, 'melodramatic': 1, 'expressions': 1, 'grief': 1}
         self.assertDictEqual(result, expected)
    
     def test_frequency_1b(self):
         text = self.load_text("test1b.txt")
         result = ds.get_frequencies(text)
         expected = {'almost': 1, 'all': 1, 'of': 8, 'shakespeares': 1, 'hamlet': 3, 'can': 1, 'be': 1, 'understood': 1, 'as': 2, 'a': 2, 'play': 1, 'about': 1, 'acting': 2, 'and': 5, 'the': 9, 'theater': 1, 'for': 4, 'example': 1, 'there': 1, 'is': 2, 'hamlets': 1, 'pretense': 1, 'madness': 1, 'antic': 1, 'disposition': 1, 'that': 1, 'he': 4, 'puts': 1, 'on': 1, 'to': 2, 'protect': 1, 'himself': 2, 'prevent': 1, 'his': 3, 'antagonists': 1, 'from': 1, 'plucking': 1, 'out': 2, 'heart': 1, 'mystery': 1, 'when': 2, 'enters': 1, 'mothers': 1, 'room': 1, 'holds': 1, 'up': 1, 'side': 2, 'by': 2, 'pictures': 1, 'two': 1, 'kings': 1, 'old': 1, 'claudius': 1, 'proceeds': 1, 'describe': 1, 'her': 1, 'true': 1, 'nature': 1, 'choice': 1, 'she': 1, 'has': 1, 'made': 1, 'presenting': 1, 'truth': 1, 'means': 1, 'show': 1, 'similarly': 1, 'leaps': 1, 'into': 1, 'open': 1, 'grave': 1, 'at': 1, 'ophelias': 1, 'funeral': 1, 'ranting': 1, 'in': 1, 'high': 1, 'heroic': 1, 'terms': 1, 'laertes': 1, 'perhaps': 1, 'well': 1, 'folly': 1, 'excessive': 1, 'melodramatic': 1, 'expressions': 1, 'grief': 1}
         self.assertDictEqual(result, expected)
    
    
class TestBigrams(unittest.TestCase):
     def test_bigrams(self):
         result = ds.find_bigrams("")
         expected = []
         self.assertListEqual(result, expected)
    
     def test_bigrams(self):
         result = ds.find_bigrams("hello world hello friends hello")
         expected = ['hello world', 'world hello', 'hello friends', 'friends hello']
         self.assertListEqual(result, expected)
    
class TestSimilarity(unittest.TestCase):
     def test_similarity1(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":2, "world":1}
         result = ds.calculate_similarity(f1, f2)
         expected = 1
         self.assertEqual(result, expected)
    
     def test_similarity2(self):
         f1 = {}
         f2 = {"hello":1}
         result = ds.calculate_similarity(f1, f2)
         expected = 0
         self.assertEqual(result, expected)
    
     def test_similarity3(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":2, "friends":1}
         result = ds.calculate_similarity(f1, f2)
         expected = .67
         self.assertEqual(round(result, 2), expected)
    
     def test_similarity4(self):
         f1 = {"hello":2, "world":1}
         f2 = {"hello":1, "friends":1}
         result = ds.calculate_similarity(f1, f2)
         expected = 0.4
         self.assertEqual(result, expected)
    
class TestGetFrequentWords(unittest.TestCase):
    def load_text(self, filename):
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

    def test_words1(self):
        f1 = {"hello":1, "world":2}
        f2 = {"hello":1, "world":5}
        result = ds.get_most_frequent_words(f1, f2)
        expected = ['world']
        self.assertListEqual(result, expected)
    
    def test_words2(self):
        f1 = {"hello":5, "world":1}
        f2 = {"hello":1, "world":5}
        result = ds.get_most_frequent_words(f1, f2)
        expected = ['hello', 'world']
        self.assertListEqual(result, expected)
    
    def test_words3(self):
        txt_3a = self.load_text('test3a.txt')
        txt_3b = self.load_text('test3b.txt')
        dict1 = ds.get_frequencies(txt_3a)
        dict2 = ds.get_frequencies(txt_3b)
        result = ds.get_most_frequent_words(dict1, dict2)
        expected = ['to']
        self.assertListEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main()
