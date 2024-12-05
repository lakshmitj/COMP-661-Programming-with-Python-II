from datetime import datetime, timedelta

#Birthday Calculator
def calculate_age(birth_date: datetime):
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day ):
        age -=1
    return age

def main():
    print("\nBirthday Calculator\n")
    while True:
        name = input("Enter name: ")
        birth_date = input("Enter birthday (MM/DD/YY): ")
        birth_date = datetime.strptime(birth_date, '%m/%d/%y')
        
        today = datetime.today()
        age = calculate_age(birth_date)
        
        # Determine the next birthday
        if (today.month, today.day) == (birth_date.month, birth_date.day ):
            days_until_next_birthday = 0
        else:
            next_birthdate = datetime(today.year, birth_date.month, birth_date.day)
            if next_birthdate < today:  # If the next birthday this year has passed
                next_birthdate = datetime(today.year + 1, birth_date.month, birth_date.day)
            
            days_until_next_birthday = (next_birthdate - today).days
        
        date_format = '%A, %B %d, %Y'
        
        print(f"\nBirthday:  {birth_date.strftime(date_format)}")
        print(f"Today:     {today.strftime(date_format)}") 
        print(f"{name.capitalize()} is {age} years old.")
        
        if days_until_next_birthday == 0:
            print(f"{name.capitalize()}'s birthday is today!")
        else:
            print(f"{name.capitalize()}'s birthday is in {days_until_next_birthday} days.")
        
        continue_choice = input("\nContinue (y/n): ")
        print()
        if continue_choice.strip().lower() != "y":
            print("Bye!")
            break


if __name__ == '__main__':
    main()
