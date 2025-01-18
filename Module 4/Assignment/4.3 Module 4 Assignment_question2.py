# Write a code segment that opens a file for input and prints 
# the number of five-letter words in the file.

import os


def get_five_letter_words(file_path, exclude_non_alphabetical_words = True):
    """
    Identifies all five-letter words in a file.

    :param file_path: Path to the input file
    :param exclude_non_alphabetical_words: Whether to exclude words with non-alphabetical characters
    :return: List of five-letter words
    """
    five_letter_words = []
    try: 
        with open(file_path, "r") as filehandler: # Opens the file in read mode ("r") and ensuring it will be properly closed after processing.
            #Iterates through each line in the file
            for line in filehandler:
                line_split = line.strip().split() # Strips whitespace and splits the line into words
                for word in line_split:
                    # checks if the length of each word is 5
                    # isalpha(): exclude words that are not purely alphabetical e.g: len("1,2,3")
                    # apply the exclude_non_alphabetical filter
                    if len(word) == 5 and (not exclude_non_alphabetical_words or word.isalpha()) : 
                        five_letter_words.append(word)
            
        return five_letter_words
      
    except FileNotFoundError:
        print(f"The file `{os.path.basename(file_path)}` does not exist.")
        return []
    except Exception as ex:
        print(f"An error occurred: {ex}")
        return []
        
def main():
    """
    Main function to handle user input and display five-letter words in a file.
    """
    file_name = "file.txt"
        
     # Update the file path based on your directory structure
    file_path = os.path.join("Module 4", "Assignment", file_name)
    
    print("\nProcessing the file...\n")

    # Exclude non-alphabetical words
    five_letter_words = get_five_letter_words(file_path) 
    print(f"The file `{file_name}` contains {len(five_letter_words)} five-letter words (excluding non-alphabetical words).")
    print(f"Words: {five_letter_words}\n")
    
     # Include non-alphabetical words
    five_letter_words_with_non_alpha = get_five_letter_words(file_path, exclude_non_alphabetical_words=False)
    print(f"The file `{file_name}` contains {len(five_letter_words_with_non_alpha)} five-letter words (including non-alphabetical words).")
    print(f"Words: {five_letter_words_with_non_alpha}\n")   
     
if __name__ == "__main__":
  main() 
