question = '''
The Python list stores a collection of objects in an ordered sequence. In 
contrast, the dictionary stores objects in an unordered collection. Give 
three examples of real-world objects that can be stored in a dictionary.
'''
print(f"{question}\n")

print("real-world objects that can be stored in a dictionary.")

#1. Customer Account Details

print("\n1.Customer Account Details:\n")
customer = {"customer_id": 1234, 
    "customer_name": "Alice", 
    "email_address": "test@test.com", 
    "address":{
        "streetAddress": "21 2nd Street",
        "city": "San Diego",
        "state": "CA",
        "postalCode": "92122"
    },
    "phoneNumber":
    [
        {
        "type": "home",
        "number": "212 555-1234"
        },
        {
        "type": "fax",
        "number": "646 555-4567"
        }
    ]
}
print(f"customer objects:\n {customer}\n")
print(f'customer name: {customer["customer_name"]}\n')
print(f'customer address: {customer["address"]["city"]}')

#2. Product Catalog 
print("\n2.Product Catalog:\n")
product_catalog = {
    "product1": {
        "id": 1,
        "name":"iPhone 9",
        "price":399,
        "description":"An apple mobile which is nothing like apple",
        "category": "smartphones"
    },
    "product2": {
        "id": 2,
        "name":"MacBook Pro",
        "price":1749,
        "description":"MacBook Pro 2021 with mini-LED display may launch between September, November",
        "category": "laptops"
    },
    "product3": {
        "id": 3,
        "name":"Samsung Galaxy Book",
        "price":1499,
        "description":"Samsung Galaxy Book S (2020) Laptop With Intel Lakefield Chip, 8GB of RAM Launched",
        "category": "laptops"
    },
    "product4": {
        "id": 4,
        "name":"OPPOF19",
        "price":299,
        "description":"OPPO F19 is officially announced on April 2021.",
        "category": "smartphones"
    }
}

print(f"Product objects:\n {product_catalog}\n")
print(f'Product Name: {product_catalog["product1"]["name"]}')
print(f'Product Category: {product_catalog["product1"]["category"]}')

#3. Student Grades

print("\n3.Student Grades:\n")
student = {
    "name": "Bob",
    "program_name": "Computer Science",
    "grade":{
        "semester1":{
         "course": [{
            "course_title": "Data Structures",
            "course_code": "CC02",
            "credit": "4",
            "int_grade": "B",
            "ext_grade": "C",
            "grade_point": "2.01",
            "letter_grade": "C",
            "credit_point": "8.05",
            "date_of_exam": "11/2015"
         },{
            "course_title": "Computation",
            "course_code": "CC03",
            "credit": "4",
            "int_grade": "B",
            "ext_grade": "C",
            "grade_point": "1.93",
            "letter_grade": "C",
            "credit_point": "7.71",
            "date_of_exam": "11/2016" 
         }]
        },
        "semester2":{
         "course": [{
          "course_title": "Design of Algorithm",
          "course_code": "CS02",
          "credit": "4",
          "int_grade": "A",
          "ext_grade": "A",
          "grade_point": "4",
          "letter_grade": "C",
          "credit_point": "9.64",
          "date_of_exam": "11/2016"
        }, {
          "course_title": "Operating system concept",
          "course_code": "CC03",
          "credit": "4",
          "int_grade": "c",
          "ext_grade": "C",
          "grade_point": "1.00",
          "letter_grade": "C",
          "credit_point": "6.71",
          "date_of_exam": "11/2016"
        }]
        }
    }
}

print(f"Product objects:\n {student}\n")
print(f"Student name: {student['name']}")
print(f"Student program: {student['program_name']}")
print(f"Student semester1 courses:\n {student['grade']['semester1']['course']}")