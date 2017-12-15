# Lab: Simple Unit Converter
## Objective

#Write a simple program that, when run, prompts the user for a number of miles,
#then prints the equivalent number of feet.
    #1. Open Atom
    #1. Create a new file and save it as `simpleunitconvert.py`
    #1. Implement the program, ideally without peeking at the solution


#miles = int(input("Enter miles: "))
#feet = miles * 5280
#print(feet)

def validate_pin(pin):
pin = input ('Enter a 4 digit or 6 digit pin: ')
if len(pin) == 4 or len(pin) == 6 and pin.isalnum():
    print (true)
else:
    return (false)

   #return true or false
