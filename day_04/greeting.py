#Write a simple program that, when run, prompts the user for their name and age,
#then prints a greeting and a message about how old they will be a year from now.

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))
age_2 = age + 1
print ("Hello %s %s, one year from now you will be %s." % (first_name, last_name, age_2))
