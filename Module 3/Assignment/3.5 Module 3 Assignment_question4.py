text = '''
Question:

Which of the following are immutable data structures? Why ? Please explain
dictionaries and lists
strings and tuples

Answer:

Immutable and Mutable Data Structures 

1.dictionaries and lists
dictionaries and lists are mutable. This means their content can be modified after they are created.

Why are they mutable:
dictionaries: we can add, update or remove key-value pairs using assignment or 
(my_dict['key'] = value) or methods like .update() or .pop().

my_dict = {"name": "Bob", "email":"test@test.com", "age": 12}

my_dict = {"name": "Bob", "email":"test@test.com", "age": 12}

#update Bob age
my_dict["age"] = 21
print(my_dict) 
#output : {'name': 'Bob', 'email': 'test@test.com', 'age': 21}
my_dict.update({"age": 25})
print(my_dict) 
#output : {'name': 'Bob', 'email': 'test@test.com', 'age': 25}

list: we can add, update or remove elements in the list using methods like .append(), .pop() or using index (my_list[0] = new_value)

my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]
my_list.append(4)
print(my_list)
my_list.pop(3)
print(my_list)

2.strings and tuples

Both strings and tuples are immutable data structures. This means their content cannot be changed once they are created.
Why are they immutable?

Strings: Each time you modify a string, a new string is created in memory because strings are immutable. This design ensures 
safety and efficiency in operations like hashing (e.g., for dictionary keys or set elements).

my_string = "hello"
my_string = my_string + " world"  # Creates a new string
print(my_string)  # Output: "hello world"

Tuples: Tuples are immutable to ensure data integrity, especially when used as keys in dictionaries or elements in sets. They provide a fixed structure that cannot be accidentally modified.

my_tuple = (1, 2, 3)
my_tuple[0] = 10 
# TypeError: 'tuple' object does not support item assignment


'''
print(text)
