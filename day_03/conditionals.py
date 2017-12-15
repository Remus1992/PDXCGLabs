#if some bool:
    #do some stuff
#if some bool:
    #do some stuff

#if 1 == 1:
#    print ('1 is equal to 1')
#if 269 == 268 + 1:
#    print ('269 is equal to 268 + 1')

name = input('What is your name?: ')
if name.lower() == 'remington':
    print ('Hi, Remington! I\'m happy to see you!')
elif name.lower() == 'katie':
    print ('Yo, {}. You are awesome!'.format(name))
else:
    print('Hi {}!'.format(name))
