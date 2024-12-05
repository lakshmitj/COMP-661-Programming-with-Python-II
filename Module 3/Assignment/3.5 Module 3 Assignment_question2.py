'''
Following the instructions, write a script that counts duplicate words.
Techniques like word frequency counting are often used to analyze published 
work. Other document analysis techniques are in natural language processing. 
Write a script that uses a dictionary to determine and print the number of 
duplicate words in a sentence. Treat uppercase and lowercase letters the same and 
assume there is no punctuation in the sentence. Words with counts larger than one 
have duplicates.

Input Text  is a tongue twister from "John Harris's Peter Piper's Practical Principles of Plain and Perfect Pronunciation" (1813):

Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked

Output Console:

WORD         COUNT
a              3
of             4
peck           4
peppers        4
peter          4
picked         4
pickled        4
piper          4
'''

def count_words(text):
    
    #lowercase input text and split into words list
    words_list = text.lower().split(" ")
    
    word_count_disc = {}

    # Count each word's occurrences
    for word in words_list:
        # if word in word_count_disc:
        #     word_count_disc[word] += 1
        # else:
        #     word_count_disc[word] = 1
        word_count_disc[word] = word_count_disc.get(word,0) + 1
    
    # Find duplicate words (count > 1)   
    duplicates_words = {word: count for word, count in word_count_disc.items() if count > 1}
    return duplicates_words

text  = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked"
duplicates_words = count_words(text)

print()
print("WORD\t\tCOUNT")
# Sort duplicates by word (ascending order) and display
for word in sorted(duplicates_words):
    print(f"{word}\t\t{duplicates_words[word]}")