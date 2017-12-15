# time = int(input('Enter time of day military time (2400 clock): '))
# if time >= 700 and  time <= 900:
#     print ("Breakfast")
# elif time >= 1200 and time <= 1400:
#     print ("Lunch")
# elif time >= 1900 and time <= 2100:
#     print ("Dinner")
# elif time >= 2200 and time <= 2400 or time >= 0 and time <= 400:
#     print ("Hammer Time")
# else:
#     print ("No time for love, Dr. Jones.")

# time = input('Enter time of day [HH:MM AM/PM])-> ') #12:30 PM
# sep_1 = " "
# t_split = time.split(sep_1,1)[-1]
# sep_2 = ":"
# minute_1 = time.split(sep_2, 1)[-1]
# minute_2 = minute_1.split (sep_1,1)[0]
#
# if t_split == "AM": #0000-1159
#     hour_1 = time.split(sep_2,1)[0]
#     hour_2 = (int(hour_1))
#
#     if hour_2 == 12:
#         hour_3 = 0
#     elif hour_2 >= 1 and hour_2 <= 11:
#         hour_3 = (hour_2) * 100
#     mil_time = hour_3 + int(minute_2)
#     print (mil_time)
#     if mil_time >= 700 and  mil_time <= 900:
#         print ("Breakfast")
#     elif mil_time == 1200
#         print ("Lunch")
#     elif mil_time >= 0 and mil_time <= 400:
#         print ("Hammer Time")
#     else:
#             print ("No time for love, Dr. Jones.")
#
# elif t_split == "PM": #1200-2359
#     hour_1 = time.split(sep_2,1)[0]
#     hour_2 = (int(hour_1))
#     if hour_2 == 12:
#         hour_3 = 1200
#     elif hour_2 >= 1 and hour_2 <= 11:
#         hour_3 = (int(hour_1) + 12) * 100
#     mil_time = hour_3 + int (minute_2)
#     print (mil_time)
#     if mil_time >= 1200 and mil_time <= 1400:
#         print ("Lunch")
#     elif mil_time >= 1900 and mil_time <= 2100:
#         print ("Dinner")
#     elif mil_time >= 2200 and mil_time <= 2400:
#         print ("Hammer Time")
#     else:
#         print ("No time for love, Dr. Jones.")


# Schedule Print Variables
breakfast = "Breakfast: 7AM - 9AM \n Eggs, Bacon, Milk"
lunch = "Lunch: 12PM - 2PM \n Hamburger, Fries, Pepsi"
dinner = "Dinner: 7PM - 9PM \n Steak, Potatoes, Beer x 2"
hammer = "HAMMER TIME \n shots, shots, shots, shots"

# 12 Hour to 24 Convert and String to Float convert
def timeconvert(time):
    # Change colon to period for float and remove spaces
    time = time.strip()
    time = time.replace(":",".")

    # Check for AM/PM and convert to float
    if "pm" in time:
        time = time.replace("pm","")
        schedule(float(time) + 12.00)

    else:
        time = time.replace("am","")
        schedule(float(time))

# Schedule Report
def schedule(timefl):
    if timefl >= 7.00 and timefl <= 9.00:
        print(breakfast)

    elif timefl >= 12.00 and timefl <= 14.00:
        print(lunch)

    elif timefl >=19.00 and timefl <= 21.00:
        print(dinner)

    elif timefl >= 22.00 or timefl <= 4.00:
        print(hammer)

    else:
        print("Food menu not available for this time... Please try again: \n")
        print("---Menu---")
        timeconvert(input("What time will you be eating? (ex. 7:30 AM): ").lower())

# Run Code
print("---Menu---")
timeconvert(input("What time will you be eating? (ex. 7:30 AM): ").lower())
