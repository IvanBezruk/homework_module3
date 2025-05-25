#Third task
import re

#Create function to normalize phone number
def normalize_phone(phone_number):
    #Delete all symbols, except numbers
    digits_only = re.sub(r'\D', '', phone_number)

    #If number starts with '380' it adds '+'
    if digits_only.startswith('380'):
        return '+' + digits_only
    
    #If number starts with '0' it adds '+38'
    if digits_only.startswith('0'):
        return '+38' + digits_only
    
    #If number is already international number it adds '+'
    if len(digits_only) > 10:
        return '+' + digits_only
    
    #Assums that in all remaning cases the number is Ukrainian without code
    return '+38' +digits_only

#User writes number
user_input = input("Enter number: ")

print(normalize_phone(user_input))