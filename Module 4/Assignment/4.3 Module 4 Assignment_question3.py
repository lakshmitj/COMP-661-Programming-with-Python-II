# Write a code segment that prints the names of all the items in the 
# current working directory.

import os
     
def list_directory_and_subfolder_contents_exclude(exclude_dirs=None, exclude_files=None):
    """
    Prints the names of all items in the current working directory,
    including the contents of sub-folders, with options to exclude specific folders or files.

    :param exclude_dirs: List of folder names to exclude
    :param exclude_files: List of file names to exclude
    """
    exclude_dirs = exclude_dirs or []  # Default to an empty list if not provided
    exclude_files = exclude_files or []  # Default to an empty list if not provided

    try:
        current_directory = os.getcwd()  # Get the current working directory
        print(f"Contents of the current directory ({current_directory}):\n")

        # Walk through the directory tree
        for root, dirs, files in os.walk(current_directory):
            # Modify `dirs` in-place to skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            print(f"Directory: {root}")
            
            # Print subdirectories
            if dirs:
                print("  Subfolders:")
                for directory in dirs:
                    print(f"    {directory}")
            else:
                print("  No subfolders.")

            # Print files, excluding the specified ones
            files_to_print = [f for f in files if f not in exclude_files]
            if files_to_print:
                print("  Files:")
                for file in files_to_print:
                    print(f"    {file}")
            else:
                print("  No files.")

            print()  # Add a blank line for readability
    except Exception as e:
        print(f"An error occurred: {e}")
        
def list_directory_and_subfolder_contents():
    """
    Prints the names of all items in the current working directory,
    including the contents of subfolders.
    """
    try:
        current_directory = os.getcwd()  # Get the current working directory
        print(f"Contents of the current directory ({current_directory}):\n")

        # Walk through the directory tree
        for root, dirs, files in os.walk(current_directory):
            print(f"Directory: {root}")
            # Print subdirectories
            if dirs:
                print("  Subfolders:")
                for directory in dirs:
                    print(f"    {directory}")
            else:
                print("  No subfolders.")

            # Print files
            if files:
                print("  Files:")
                for file in files:
                    print(f"    {file}")
            else:
                print("  No files.")
            
            print()  # Add a blank line for readability
    except Exception as e:
        print(f"An error occurred: {e}")

def list_directory_contents():
    """
    Prints the names of all items in the current working directory.
    """
    try:
        current_directory = os.getcwd()  # Get the current working directory
        print(f"\nContents of the current directory ({current_directory}):\n")

        # List all items in the current directory
        items = os.listdir(current_directory)

        if items:
            for item in items:
                print(item)
        else:
            print("The directory is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
   
def menu():
      
    """Display menu options and perform actions based on user choice."""
    while True:
        print("\nMenu:")
        print("1. List directory contents")
        print("2. List directory and subfolder contents")
        print("3. List directory and subfolder contents(with exclude option)")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            list_directory_contents()
        elif choice == "2":
            list_directory_and_subfolder_contents()
        elif choice == "3":
             # Specify folders and files to exclude
            exclude_dirs = [".git", ".gitignore"]
            exclude_files = ["readme.md", ".DS_Store"]
            list_directory_and_subfolder_contents_exclude(exclude_dirs=exclude_dirs, exclude_files=exclude_files)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    menu()