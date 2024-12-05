'''
 Create a program that a user can use to manage the primary email address and phone number for a contact.

a. Use a multi-dimensional list to store the data for the contacts. Provide starting data for two or more contacts.

b.  For the view and del commands, display an error message if the user enters an invalid contact number.

c. When you exit the program, all changes that you made to the contact list are lost.
'''
#Python list
user_contacts = [
    [ "Marilyn Monroe", "MarilynMonroe@gmail.com", "+22 33 4567 4588"],
    [ "Abraham Lincoln", "AbrahamLincoln@whitehouse.org", "+22 33 4567 4587"]
]
    
def display_menu():
    print()
    print("Contact Manager\n")
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contact")
    print("exit - Exit program")
    print()

def display_user_contacts():
    
    """Displays all contacts"""
    print("\nCommand: list")
    
    i = 1
    for contact in user_contacts:
        print(f"{i}. {contact[0]}")
        i += 1
    print()

def view_user_contact(contact_index:int):
    
    """View a contact"""
    print("\nCommand: view")
    
    if contact_index < 0 or contact_index >= len(user_contacts):
        print("Invalid contact number")
        return 0
           
    contact = user_contacts[contact_index]
    print(f"Number: {contact_index+1}\nName: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
    print()
    
def add_contact():
    
    """Add a contact"""
    print("\nCommand: add")
    
    name = input("Name: ")
    email_address = input("Email: ")
    phone_number = input("Phone:")
    user_contacts.append([name,email_address,phone_number])
    print(f"{name} was added")
    print()
    
def delete_contact(contact_index):
    """Delete a contact"""
    print("\nCommand: del")
    
    if contact_index < 0 or contact_index >= len(user_contacts):
        print("Invalid contact number.")
        return 0
           
    contact = user_contacts[contact_index]
    user_contacts.pop(contact_index)
    print(f"Number: {contact_index+1}\n{contact[0]} was deleted.")
    print()
    
def main():
    
    display_menu()
    while(True):
        command = input("Enter command:")
        if command.lower() == 'list':
            display_user_contacts()
        elif command.lower() == 'view':
            try:
                contact_index = int(input("Enter contact number you like to view: "))
                if view_user_contact(contact_index-1) == 0:
                    break
            except ValueError:
                print("Invalid contact number.")
        elif command.lower() == 'add':
            add_contact() 
        elif command.lower() == 'del':
            try:
                contact_index = int(input("Enter contact number you like to delete: "))
                if delete_contact(contact_index-1) == 0:
                    break
            except ValueError:
                print("Invalid contact number.")
        elif command.lower() == 'exit':
            print("Bye!")
            break
        else:
            print("This is not a valid command. Please try again.")
            
        


if __name__ == "__main__":
    main()
