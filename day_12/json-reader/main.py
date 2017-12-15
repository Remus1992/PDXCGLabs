import json
data = json.load(open('data.json'))

for x in data:
    print("The Latitude/ Longitude of %s is %s/ %s." % (x, data[x]["Position"]['Latitude'], data[x]["Position"]['Longitude']))



# from pprint import pprint
# pprint (data)

# data["Portland"]["Position"]

# pprint (data)
# pprint (data["Portland"]["Position"])
# pprint (data["Portland"]["Position"]['Latitude'])
# pprint (data["Portland"]["Position"]['Longitude'])
