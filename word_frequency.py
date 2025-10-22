#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    user_sentence = input("Enter a sentence: ")
    sentence = user_sentence.split(" ")
     sentence = []
    for word in input_sentence:
        word = word.lower().strip(".,!?")
        if word != "":  
            sentence += [word]
    return sentence

def calculate_frequencies(sentence):
    words = []
    frequencies = []

    for word in sentence:
            found = False
            for i in range(len(words)):
                if words[i] == word:
                    frequencies[i] = frequencies[i] + 1
                    found = True
                    break
            if not found:
                words = words + [word]
                frequencies = frequencies + [1]
    return words, frequencies 


def print_frequencies(words, frequencies):
    for i in range(len(words)):
        print(words[i] + ":", frequencies[i])  

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

main()
