#Second task
import random

#Create a function that generates unique random values for lotery
def get_numbers_ticket(min, max, quantity):
    
    #Check task requerements
    if min <1 or max > 1000 or quantity > (max - min +1) or min > max :
        return []
    
    #Generate unique numbers and sort them
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)