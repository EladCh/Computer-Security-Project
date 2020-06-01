
from bloomfilter import BloomFilter 
from random import shuffle 
from tkinter import *
import PySimpleGUI as sg 
from password_strength_rules import password_rules

# n = 20 #no of items to add 
# p = 0.05 #false positive probability 
  
# bloomf = BloomFilter(n,p) 
# print("Size of bit array:{}".format(bloomf.size)) 
# print("False positive Probability:{}".format(bloomf.fp_prob)) 
# print("Number of hash functions:{}".format(bloomf.hash_count)) 
  
# # words to be added 
# word_present = ['abound','abounds','abundance','abundant','accessable', 
#                 'bloom','blossom','bolster','bonny','bonus','bonuses', 
#                 'coherent','cohesive','colorful','comely','comfort', 
#                 'gems','generosity','generous','generously','genial'] 
  
# # word not added 
# word_absent = ['bluff','cheater','hate','war','humanity', 
#                'racism','hurt','nuke','gloomy','facebook', 
#                'geeksforgeeks','twitter'] 
  
# for item in word_present: 
#     bloomf.add(item) 
  
# shuffle(word_present) 
# shuffle(word_absent) 
  
# test_words = word_present[:10] + word_absent 
# shuffle(test_words) 
# for word in test_words: 
#     if bloomf.check(word): 
#         if word in word_absent: 
#             print("'{}' is a false positive!".format(word)) 
#         else: 
#             print("'{}' is probably present!".format(word)) 
#     else: 
#         print("'{}' is definitely not present!".format(word)) 


def test_bloom_filter(num_of_items, fp_prob):
    bloomf = BloomFilter(num_of_items,fp_prob) 
    
    # words to be added 
    word_present = ['abound','abounds','abundance','abundant','accessable', 
                    'bloom','blossom','bolster','bonny','bonus','bonuses', 
                    'coherent','cohesive','colorful','comely','comfort', 
                    'gems','generosity','generous','generously','genial']
    
    # word not added
    word_absent = ['bluff','cheater','hate','war','humanity', 
                'racism','hurt','nuke','gloomy','facebook', 
                'geeksforgeeks','twitter']
    
    top_passwords_last_years = ['123456',	'123456789', 'qwerty', 'password',
                                'football', '1234567', '12345678', 'letmein',
                                '1234', '1234567890', 'dragon', 'baseball',
                                'sunshine', 'iloveyou','trustno1', 'princess',
                                'adobe123', '123123', 'welcome', 'login', 'admin',
                                '111111', 'qwerty123', 'solo', '1q2w3e4r', 'master',
                                'abc123', '666666', 'photoshop', '1qaz2wsx', 'qwertyuiop',
                                'ashley', 'mustang', '121212', 'starwars',	'654321',
                                'bailey',	'access', 'flower', '555555', 'passw0rd',
                                'monkey', 'lovely', 'shadow', '7777777', '12345', 'michael',
                                '!@#$%^&*', 'jesus', 'password1', 'superman', 'hello',
                                'charlie', '888888', '696969', 'hottie', 'freedom', 'aa123456',
                                'qazwsx', 'ninja', 'azerty', 'loveme', 'whatever', 'donald',
                                'batman', 'zaq1zaq1', 'Football', '0', '123qwe', '1111111',
                                '12345', '000000', '1234', '1q2w3e4r5t', '123', '987654321',
                                '12345679', 'mynoob', '123321', '18atcskd2w', '3rjs1la7qe',
                                'google', 'zxcvbnm', '1q2w3e', ]
    
    for item in word_present:
        bloomf.add(item)

    shuffle(word_present) 
    shuffle(word_absent)
    
    test_words = word_present[:10] + word_absent 
    shuffle(test_words)
    
    for word in test_words:
        if bloomf.check(word):
            if word in word_absent:
                print("'{}' is a false positive!".format(word))
            else:
                print("'{}' is probably present!".format(word))
        else:
            print("'{}' is definitely not present!".format(word))
    
    # words = word_present + word_absent
    # password_rules(words)


