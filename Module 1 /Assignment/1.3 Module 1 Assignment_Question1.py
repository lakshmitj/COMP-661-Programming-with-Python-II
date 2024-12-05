from datetime import datetime, timedelta

#calculate trip travel time
def get_departure_date():
    departure_date = input("Estimated date of departure (YYYY-MM-DD): ")
    departure_time = input("Estimated time of departure (HH:MM AM/PM): ")
    departure_datetime = datetime.strptime(f"{departure_date} {departure_time}", "%Y-%m-%d %I:%M %p")
    return (departure_datetime)


def main():
    
    print("\nArrival Time Estimator\n")
     
    while(True):
        try:
            departure_datetime = get_departure_date()
            #print(departure_datetime)
            
            while(True):
                try:
                    miles = int(input("Enter miles: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for miles.")
                    
            while(True):
                try:
                    speed = int(input("Enter miles per hour: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for speed.")
                    
            total_time_in_hours = miles/speed
            hours = int(total_time_in_hours)
            minutes = int((total_time_in_hours - hours) * 60)
            
            print("\nEstimated travel time\n")
            print(f"Hours: {hours}")
            print(f"Minutes: {minutes}")
            
            travel_time = timedelta(hours=hours, minutes=minutes)
            arrival_datetime = departure_datetime + travel_time 
            
            print(f"Estimated date of arrival: {arrival_datetime.strftime('%Y-%m-%d')}")
            print(f"Estimated time of arrival: {arrival_datetime.strftime('%I:%M %p')}")
            
            continue_choice = input("Continue (y/n):")
            print()
            if continue_choice.strip().lower() != "y":
                print("Bye!")
                break
        except ValueError as e:
            print(f"Invalid input. Please try again.\nError: {e}")
        except ZeroDivisionError:
            print("Speed cannot be zero. Please try again.")

if __name__ == '__main__':
    main()