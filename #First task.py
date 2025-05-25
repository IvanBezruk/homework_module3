#First task
import datetime

#We create a functin that calculates how many days are between today's date and specific date
def get_days_from_today(date):
    #Skip if user entered incorrect format of date
    try:

        #Convert the input string to a datetime oject
        written_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        #Determination of taday's date
        current_date = datetime.date.today()

        #Calculate the difference in days
        difference = current_date - written_date

        #Return the difference in days
        return difference.days
    
    except ValueError:
        #if format is wron the program shows message
        print(f"Incorrect date format: '{date}'. Please use YYYY-MM-DD format.")
        return None

#Show results as stated in the task
print(get_days_from_today('2020-10-09'))

#Ask user to enter a date
user_input = input("Enter a date in YYYY-MM-DD format: ")

#Show results per user input
print(get_days_from_today(user_input))
