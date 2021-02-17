# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 07:41:35 2020

@author: User
"""


def print_vowel_count():
    vowels = ['a','e','i','o','u'] 
    # get user input
    # assign it to word
    # word = get_user_input()    
    word = 'azcbobobegghakl'
    for i in range(len(word)):
        print(str(word(j)))
        for j in range(len(vowels)):
            if word[i] == vowels[j]:
                count += 1
                break
    print(str)
print_vowel_count()