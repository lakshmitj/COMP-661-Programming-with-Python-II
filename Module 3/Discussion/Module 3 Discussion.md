1. Discuss the difference between a mutable and immutable collection.

## mutable collection:
- Mutable collections can be modified after they are created.
- Operations like adding, updating, or deleting elements can be performed on mutable objects
- examples in Python: list , set, dict
## immutable collection:
- Immutable collections cannot be changed after they are created.
- Any operation that appears to modify an immutable object creates a new object instead.
- Examples in Python: tuple, frozenset, string.
2. How does Python handle mutable and immutable objects differently? 

In Python, mutable and immutable objects are handled differently due to their distinct properties:

Mutability:

Mutable objects: Can be modified after they are created 

       Examples include: Lists (list) , Dictionaries (dict), Sets (set), Byte arrays (bytearray)

Immutable objects: Cannot be modified after they are created.

Examples include: Strings (str), Tuples (tuple), Numbers (int, float, complex), Frozensets (frozenset)

Memory Management:

Mutable Objects: The same memory location is reused when the object is modified.

Examples

my_list = [1, 2, 3]
print(id(my_list))  # Memory address of `my_list`
my_list.append(4)
print(id(my_list))  # Same memory address, list is updated

Immutable Objects: A new object is created whenever the value changes.

Example:

my_string = "hello"
print(id(my_string))  # Memory address of `my_string`
my_string += " world"
print(id(my_string))  # Different memory address, new string created

Argument Passing in Functions:

Mutable Objects: Changes made to the object within a function persist outside the function because the function operates on the original object.

Example:

def modify_list(lst):
    lst.append(4)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # Output: [1, 2, 3, 4]

Immutable Objects: Functions cannot modify the original object; instead, they operate on a copy or create a new object.

Example:

def modify_string(s):
    s += " world"

text = "hello"
modify_string(text)
print(text)  # Output: "hello" (unchanged)

Performance Implications:

Immutable objects are generally more memory-efficient for certain use cases (e.g., strings and tuples are often reused internally by Python).
Mutable objects are more flexible but may lead to unintended side effects if shared across parts of a program.

Hashability:

Immutable objects are hashable (can be used as dictionary keys or set elements) because their values cannot change.

Example:

my_dict = {("x", "y"): "coordinates"}  # Tuple as a key


Mutable objects are not hashable because their values can change

Example:

my_dict = {[1, 2, 3]: "list key"}  # Raises a TypeError


3. How does that apply to Python dictionaries?

Dictionaries are Mutable: 

Can be modified in place (add, update, or delete key-value pairs) without creating a new dictionary.

eg:

my_dict = {"a": 1, "b": 2}
print(id(my_dict))  # Memory address of `my_dict`

my_dict["c"] = 3  # Add a new key-value pair
print(id(my_dict))  # Memory address remains the same
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

Keys Must Be Immutable:

Keys must be hashable (e.g., int, str, tuple with immutable elements).
Mutable types like list , dict or  cannot be keys.
Immutable types like int, float, str, tuple (with immutable elements) are allowed to be keys - eg: my_dict = {[1, 2, 3]: "value"}  # TypeError: unhashable type: 'list'
If you use a tuple as a key, it must contain only immutable elements:

eg:

valid_key = (1, 2, "a")
invalid_key = ([1, 2], "a")  # Contains a mutable list

my_dict = {valid_key: "value"}  # Works

Passing to Functions:

Dictionaries are passed by reference, meaning changes made in functions affect the original dictionary. Use .copy() or copy.deepcopy() to avoid side effects.
In Functions: When a dictionary is passed to a function, the function can modify the original dictionary because it operates on the same memory reference. This can lead to side effects.
To avoid unintended modifications, pass a copy of the dictionary

eg:

def add_entry(d):
    d["new_key"] = "new_value"

my_dict = {"a": 1}
add_entry(my_dict.copy())  # Original dictionary remains unchanged
print(my_dict)  # Output: {'a': 1}

Nested Mutability: Modifying mutable objects (e.g., lists) inside a dictionary affects the original dictionary unless a deep copy is used.

eg:nested_dict = {"a": [1, 2, 3]}
nested_dict["a"].append(4)  # Modifying the list in place
print(nested_dict)  # Output: {'a': [1, 2, 3, 4]}.    

         To create a completely independent copy, use copy.deepcopy:

import copy

nested_dict = {"a": [1, 2, 3]}
new_dict = copy.deepcopy(nested_dict)
new_dict["a"].append(4)

print(nested_dict)  # Output: {'a': [1, 2, 3]} (unchanged)
print(new_dict)     # Output: {'a': [1, 2, 3, 4]}




Dynamic Views:

Dictionary views (dict.keys(), dict.values(), dict.items()) are dynamic and reflect changes in thedictionary because they reference the same underlying data.

e.g:

my_dict = {"a": 1, "b": 2}
keys_view = my_dict.keys()

my_dict["c"] = 3
print(keys_view)  # Output: dict_keys(['a', 'b', 'c']) (updated)




4. How would this apply to a real-world situation?

In real-world programming, the mutability of dictionaries influences how we handle data structures, APIs, configuration settings, or any scenario involving shared data.

Here are some  examples:

 API Data Handling:  Processing JSON data from an API, which Python loads as a dictionary.

Risk: Mutating the dictionary directly could overwrite critical data.

Example: 

user_data = {"name": "Alice", "age": 30}

def anonymize(data):
    data["name"] = "Anonymous"  # Direct modification

anonymize(user_data)
print(user_data)  # Output: {'name': 'Anonymous', 'age': 30}

Solution: Work on a copy of the data

Example:

def anonymize(data):
    modified_data = data.copy()
    modified_data["name"] = "John"
    return modified_data

anonymized = anonymize(user_data)
print(user_data)     # Output: {'name': 'Alice', 'age': 30}
print(anonymized)    # Output: {'name': 'John', 'age': 30}

Nested Data Structures:  Managing nested dictionaries, such as JSON data.

Risk: Modifying a nested dictionary affects the original data unexpectedly.

Example:

company = {"name": "TechCorp", "departments": {"IT": {"employees": 50}}}

def update_employees(data):
    data["departments"]["IT"]["employees"] += 10

update_employees(company)
print(company)  # Output: {'name': 'TechCorp', 'departments': {'IT': {'employees': 60}}}

Solution: Use copy.deepcopy to avoid altering nested structures.

import copy

def update_employees(data):
    data_copy = copy.deepcopy(data)
    data_copy["departments"]["IT"]["employees"] += 10
    return data_copy

updated_company = update_employees(company)
print(company)         # Output: {'name': 'TechCorp', 'departments': {'IT': {'employees': 50}}}
print(updated_company) # Output: {'name': 'TechCorp', 'departments': {'IT': {'employees': 60}}}