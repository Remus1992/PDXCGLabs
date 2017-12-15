funny_job = input('List a funny occupation: ')
thing = input('Type a thing: ')
place = input('Enter a place: ')
describing_word = input ('Enter a describing word: ')
thing_2 = input ('Type another thing: ')
difficult_thing = input ('Now enter something difficult to do: ')
action = input ('Enter an action: ')
amount_time = input ('Enter an amount of time: ')
thing_3 = input ('Enter a third thing: ')
something_read = input ('What is the last book you read?: ')
MadLib = '''\nWell, I was born a {funny_job}'s daughter
In a {thing} on a hill in {place}
We were {describing_word} but we had {thing_2},
That's the one thing that daddy made sure of
He {difficult_thing} to make a poor man's dollar.
My daddy {action} {amount_time} in the Vanleer coal mine
All long in the field a-hoin' corn.
Mommie rocked the {thing_3} at night, and read the {something_read} by the coal-oil light
And ever'thing would start all over come break of morn' '''. format (funny_job = funny_job, thing = thing, place = place,
 describing_word = describing_word, thing_2 = thing_2, difficult_thing = difficult_thing,
 action = action, amount_time = amount_time, thing_3 = thing_3, something_read = something_read)
print (MadLib)
