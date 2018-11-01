#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

__author__ = "bomazani"


import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    """ Creates a dictionary with each unique word as the keys, 
    and values = each word that immediately follows the key(including duplicates)."""
    with open(filename, "r") as f:
        file_split = f.read().split()
        word_dict = {}
        prev_string = ''
        for word in file_split:
            if prev_string not in word_dict:
                word_dict[prev_string] = [word]
            else:
                word_dict[prev_string].append(word)
            prev_string = word

    return word_dict



# # raise NotImplementedError("Get to Work!")


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""  
    for _ in range(200):
        print word,
        next_word_list = mimic_dict.get(word)
        if not next_word_list:
            next_word_list = mimic_dict['']
        word = random.choice(next_word_list)

    
    # raise NotImplementedError("Get to Work!")
   

# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print 'usage: python mimic.py file-to-read'
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
