'''
5.Create a file called accounts.txt and enter the following information in the file
100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Zoltar -32.16
500 Kathleen 24.32

6. In the accounts.txt file:

update the name 'Zoltar' to 'Robert' 
create a tempfile with the new data
remove accounts.txt file from the directory
rename the tempfile to a new file called myaccounts.txt
'''

import os
from pathlib import Path


def create_accounts_file(file_path: Path):
    """Create the accounts.txt file with initial content."""
    accounts_content = """100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Zoltar -32.16
500 Kathleen 24.32"""
    
    with open(file_path, "w") as file:
        file.write(accounts_content)
    print(f"File `{file_path.name}` created with initial content.")
    
def update_name_in_file(file_path: Path):
    """Update the name 'Zoltar' to 'Robert' and save to a temporary file."""
    
    if not file_path.is_file():
        print(f"Error: `{file_path.name}` file does not exist. Please create it first.")
        return

    tempfile_path =  Path(os.path.join(os.path.dirname(__file__), "tempfile.txt")).absolute()
    with open(file_path, "r") as input_file, open(tempfile_path, "w") as output_file:
        for line in input_file:
            updated_line = line.replace("Zoltar", "Robert")
            output_file.write(updated_line)
    print(f"Updated content written to `{tempfile_path.name}`.")
    
def remove_accounts_file(file_path: Path):
    """Remove the accounts.txt file."""
    if file_path.is_file():
        file_path.unlink()
        print(f"`{file_path.name}` has been removed.")
    else:
        print(f"Error: `{file_path.name}` file does not exist.")
        
def rename_tempfile():
    """Rename the temporary file to myaccounts.txt."""
    tempfile_path =  Path(os.path.join(os.path.dirname(__file__), "tempfile.txt")).absolute()

    if tempfile_path.is_file():
        new_file_path = tempfile_path.rename(Path(os.path.join(os.path.dirname(__file__), "myaccounts.txt")).absolute())
        print(f"`{tempfile_path.name}` renamed to `{new_file_path.name}`.")
    else:
        print(f"Error: `{tempfile_path.name}` does not exist. Please update the name first.")

def display_myaccounts():
    """Display the content of myaccounts.txt."""
    file_path =  Path(os.path.join(os.path.dirname(__file__), "myaccounts.txt")).absolute()
    if file_path.exists():
        with open(file_path, "r") as file:
            content = file.read()
        print(f"\nContent of {file_path.name:}")
        print(content)
    else:
        print(f"Error: {file_path.name} file does not exist.")

        
def menu():
    
    file_name = "accounts.txt"
    file_path = Path(os.path.join(os.path.dirname(__file__), "accounts.txt")).absolute()
    
    """Display menu options and perform actions based on user choice."""
    while True:
        print("\nMenu:")
        print("1. Create accounts.txt file")
        print("2. Update 'Zoltar' to 'Robert'")
        print("3. Remove accounts.txt file")
        print("4. Rename tempfile to myaccounts.txt")
        print("5. Display content of myaccounts.txt")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            create_accounts_file(file_path)
        elif choice == "2":
            update_name_in_file(file_path)
        elif choice == "3":
            remove_accounts_file(file_path)
        elif choice == "4":
            rename_tempfile()
        elif choice == "5":
            display_myaccounts()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
   menu()
    
    