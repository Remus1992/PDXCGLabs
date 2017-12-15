class Car:
    def __init__(self, brand, color, number_of_doors):
        self.brand = brand
        self.color = color
        self.number_of_doors = number_of_doors
        self.number_of_wheels = 4

    def honk(h):
        if h == 'Y' or h == 'y':
            print ('[INSERT: Linda Belcher voice: HONK!')
        elif h == 'N' or h == 'n':
            print ('Fine, I won\'t. Your loss.')
        else:
            print ('Can\'t you follow simple instructions?')



brand_01 = Car('Toyota', 'Green', '4')
brand_02 = Car('Suburu', 'Blue', '2')

print (brand_01.brand)
print (brand_01.color)
print (brand_01.number_of_doors)
print (brand_01.number_of_wheels)

print (brand_02.brand)
print (brand_02.color)
print (brand_02.number_of_doors)
print (brand_02.number_of_wheels)
