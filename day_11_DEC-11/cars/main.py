from car import Car

brand_03 = Car('Mazda', 'Yellow', '5')


print (brand_03.brand)
print (brand_03.color)
print (brand_03.number_of_doors)
print (brand_03.number_of_wheels)

honk = input("Do You Want to Honk? Y/N: ")
Car.honk(honk)
