# Impledge_WordCompositionProblem

"I've developed a program to find the longest and second-longest compound words in a given list of words. Let me walk you through it:

Class CompoundWordFinder:
This class encapsulates all the functionality needed to find compound words in a list.
Initializer (__init__):
It takes the file path as input and initializes the word lists.
Method read_words_from_file:
This method reads words from the file and stores them in a list and a set for efficient lookups.
Method is_construction_possible:
It checks if a word can be constructed from other words in the list. It does this recursively by splitting the word into prefix and suffix and checking if both can be found in the word list.
Method find_longest_compound_words:
This method finds the longest and second-longest compound words in the list. It first sorts the words by length and then iterates through them to find the longest and second-longest compound words.
Main Section:
Here, we initialize the CompoundWordFinder for each file and find the longest and second-longest compound words for each file.
