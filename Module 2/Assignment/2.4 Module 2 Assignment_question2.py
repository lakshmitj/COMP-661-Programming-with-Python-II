'''
 Insert 10 random letters in the range ‘a’ through ‘z’ into a list. Perform the 
 following tasks and display your results

a. Sort the list in ascending order

b. Sort the list in descending order

c. Get the unique values sort them in ascending order
'''
import random
import string

random_letters = [random.choice(string.ascii_lowercase) for _ in range(10)]
print(f"Random Letters\n{random_letters}")

# a. Sort the list in ascending order
sorted_list_asc = sorted(random_letters)
print(f"Sort the list in ascending order.\n{sorted_list_asc}")

# b. Sort the list in descending order
sorted_list_desc = sorted(random_letters, reverse=True)
print(f"Sort the list in descending order.\n{sorted_list_desc}")

# c. Get unique values and sort them in ascending order
unique_sorted_list = sorted(set(random_letters))
print(f"Unique values sorted in ascending order.\n{unique_sorted_list}")
