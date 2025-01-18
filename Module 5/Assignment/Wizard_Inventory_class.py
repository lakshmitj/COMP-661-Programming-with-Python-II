import os
import random

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

BASE_DIR = os.getcwd()
ITEMS_FILENAME = os.path.join(BASE_DIR, ITEMS_FILENAME)
INVENTORY_FILENAME = os.path.join(BASE_DIR, INVENTORY_FILENAME)

class WizardInventory:
    def __init__(self, items_filename="wizard_all_items.txt", inventory_filename="wizard_inventory.txt"):
        self.items_filename = items_filename
        self.inventory_filename = inventory_filename

    def _read_items(self):
        """Reads available items from the items file."""
        items = []
        try:
            with open(self.items_filename) as file:
                for line in file:
                    items.append(line.strip())
            return items
        except FileNotFoundError:
            print(f"Could not find the items file.\n")
            print("Exiting program. Bye!\n")
            exit(1)

    def _read_inventory(self):
        """Reads the inventory from the inventory file."""
        inventory = []
        try:
            with open(self.inventory_filename) as file:
                for line in file:
                    inventory.append(line.strip())
            return inventory
        except FileNotFoundError:
            print(f"\nCould not find inventory file!")
            return inventory

    def _write_inventory(self):
        """Writes the current inventory to the inventory file."""
        with open(self.inventory_filename, "w") as file:
            for item in self.inventory:
                file.write(item + "\n")
            
    def delete_inventory_file(self):
        if os.path.exists(self.inventory_filename):
            os.remove(self.inventory_filename)

    def display_title(self):
        """Displays the program title."""
        print("\nThe Wizard Inventory program\n")

    def display_menu(self):
        """Displays the command menu."""
        print("COMMAND MENU")
        print("walk - Walk down the path")
        print("show - Show all items")
        print("drop - Drop an item")
        print("exit - Exit program\n")

    def walk(self):
        """Simulates the 'walk' action, allowing the wizard to pick up items."""
        try:
            items = self._read_items()
            item = random.choice(items)
            print(f"While walking down a path, you see {item}.")
            choice = input("Do you want to grab it? (y/n): ").strip().lower()
            if choice == "y":
                if len(self.inventory) >= 4:
                    print("You can't carry any more items. Drop something first.\n")
                else:
                    self.inventory.append(item)
                    print(f"You picked up {item}.\n")
                    self._write_inventory()
        except IndexError:
            print("Error: No items available. Exiting program.")
            exit(1)
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

    def show_inventory(self):
        """Displays all items in the inventory."""
        if self.inventory:
            for i, item in enumerate(self.inventory, start=1):
                print(f"{i}. {item}")
        else:
            print("Your inventory is empty.")
        print()

    def drop_item(self):
        """Allows the user to drop an item from their inventory."""
        try:
            number = int(input("Number: "))
            if 1 <= number <= len(self.inventory):
                item = self.inventory.pop(number - 1)
                print(f"You dropped {item}.\n")
                self._write_inventory()
            else:
                print("Invalid item number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def run(self):
        """Runs the main program loop."""
        self.display_title()
        self.display_menu()
        
        self.inventory = self._read_inventory()
        if not self.inventory:
            print(f"Wizard is starting with no Inventory\n")
    

        while True:
            command = input("Command: ").strip().lower()
            if command == "walk":
                self.walk()
            elif command == "show":
                self.show_inventory()
            elif command == "drop":
                self.drop_item()
            elif command == "exit":
                self.delete_inventory_file()
                print("Bye!")
                break
            else:
                print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    wizard_inventory = WizardInventory()
    wizard_inventory.run()
