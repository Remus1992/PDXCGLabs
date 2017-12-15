'''
Fizz Buzz
1. Fizz if N divisable by 3
2. Buzz if N divisable by 5
3. Fizz Buzz if N divisable by 3 & 5
4. N if N is not divisable by 3 or 5
'''

def fizz_buzz(n):
    num = n
    if n % 3 == 0 & n % 5 == 0:
        print ("Fizz Buzz")

    elif n % 3 == 0:
        print ("Fizz")

    elif n % 5 == 0:
        print ("Buzz")

    else:
        print ("%s is not a Fizz or a Buzz" % num)

def prompt():
    while True:
        option = input ("Do you wish to enter a number (N) or exit (E): ")
        if option == 'n':
            fizz_buzz(int(input("Enter a number: ")))
        elif option == 'e':
            print ("Goodbye!")
            break
        else:
            print ("Not a valid option. Try again.")

prompt()
