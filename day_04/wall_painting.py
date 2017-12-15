import math
wall_width = float(input("Enter the Width of your Wall: "))
wall_height = float(input("Enter the Height of your Wall: "))
gallon_cost = float(input("What's the cost of your paint?: $ "))
coats_paint = int(input("How many coats of paint are you going to use?: "))

area_wall = wall_width * wall_height
gallons_needed = math.ceil ((coats_paint * area_wall) / 400)

total_gallon_cost = gallon_cost * gallons_needed

print ("The area of your wall is %s. Using %s coats, you will need %s gallons to paint that wall. Your total cost will be $%s" % (area_wall, coats_paint, gallons_needed, total_gallon_cost))

#
# area_wall = wall_width * wall_height
# gallons_needed = math.ceil (area_wall / 400)
# gallons_needed_w_coats = gallons_needed * coats_paint
# total_gallon_cost = gallon_cost * gallons_needed_w_coats
#
# print ("The area of your wall is %s. Using %s coats, you will need %s gallons to paint that wall. Your total cost will be $%s" % (area_wall, coats_paint, gallons_needed_w_coats, total_gallon_cost))
