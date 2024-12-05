question1 = '''
1.What does this code do?

The dictionary temperatures contain four Fahrenheit samples for each of 
five days. What does the “for” statement do?

temperatures = {
'Monday': [67, 71, 74, 77],
'Tuesday': [52, 56, 66 , 50],
'Wednesday': [77, 80, 87 , 95],
'Thursday': [67, 77, 81 , 77],
'Friday': [54 , 60 , 67, 60],
}
for k, v in temperatures.items():
     print(f'{k}: {sum(v)/len(v):.0f}')
'''
print(question1)

print("Response:\n")
answer = '''

The for statement iterates through the key, value paries on the dictionary using .items() method
k - key e.g: Monday
v - value e.g: [67, 71, 74, 77]

for loop:

For each key in dictionary temperatures, finds the the average temperature for the list of values(v)
sum(v): add all the temperatures (e.g: 67+71+74+77= 289)
len(v): number of temperatures in list v (e.g: len(v) =5
sum(v)/len(v): division to calculate the average temperature

print statement output the day(k) with average temperature rounded to nearest whole number(:.0f)

output:

Monday: 72
Tuesday: 56
Wednesday: 85
Thursday: 76
Friday: 60

'''

print(answer)