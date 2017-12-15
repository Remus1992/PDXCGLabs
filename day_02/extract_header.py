# Lab: Extract Header

#Write a python function to parse a string containing email address data for the first matching domain name.
#Example: chris@pdxcodeguild.com should print as "pdxcodeguild".

##### Instructions

#Think string methods, and slicing.  Use the `@` and `.com` characters location to determine slice start and stop positions.

#### Documentation

#1. [Python Official: str.index()](https://docs.python.org/3.6/library/stdtypes.html#str.index)
#1. [Python Official: string tutorial](https://docs.python.org/3.6/tutorial/introduction.html#strings)

#### Key Concepts
#- String methods
#- String slicing

email = input("Enter email: ")
sep = "@"
rest = email.split(sep,1)[-1]
sep_2 = "."
rest_2 = rest.split(sep_2,1)[0]
print (rest_2)
