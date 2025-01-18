# Write a code segment that opens a file named file.txt for input and 
# prints the number of lines in that file. 

import os
from pathlib import Path

def read_file_contents():
    """
    Prompts the user for a file, prints its contents if it exists, 
    or displays an error message if the file does not exist.
    """
    file_name = input("Enter the file name with its extension: ").strip()
    
    file_path = Path(os.path.join(os.path.dirname(__file__), file_name)).absolute()
    
    # Check if the file exists
    if not file_path.is_file():
        print(f"Error: The file '{file_name}' does not exist.")
        return
    
    try:
        # Open and read the file contents
        with open(file_path, "r") as file:
            print(f"\nContents of '{file_name}':\n")
            print(file.read())
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    read_file_contents()