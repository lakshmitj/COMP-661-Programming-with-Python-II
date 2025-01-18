# Write a code segment that opens a file named file.txt for input and 
# prints the number of lines in that file. 

import os

def get_file_line_count(file_path):
    """
    Counts the number of non-empty lines in the given file.

    :param file_path: Path to the file
    :return: Number of non-empty lines in the file
    """
    try: 
        with open(file_path, "r") as filehandler: # Opens the file in read mode ("r") and ensuring it will be properly closed after processing.
            # Iterate through each line in the file and count non-empty lines
            line_count = sum(1 for line in filehandler if line.strip())
            
        return line_count
      
    except FileNotFoundError:
        print(f"The file `{os.path.basename(file_path)}` does not exist.")
        return 0
    except Exception as ex:
        print(f"An error occurred: {ex}")
        return 0
        
        
def main():
    file_name = "file.txt"
    
    # Update the file path based on your directory structure
    file_path = os.path.join("Module 4", "Assignment", file_name)
    
    file_line_count = get_file_line_count(file_path)
    
    if file_line_count:
        print(f"The file `{file_name}` contains {file_line_count} non-empty lines.")
    else:
        print(f"Could not count lines in the file `{file_name}`.")
    
if __name__ == "__main__":
  main() 
