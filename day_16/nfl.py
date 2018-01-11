conferences = {
"AFC":{
    "East":
        [
        "Buffalo Bills",
        "Miami Dolphins",
        "New England Patriots",
        "New York Jets"
        ],
    "North":
        [
        "Baltimore Ravens",
        "Cincinnati Bengals",
        "Cleveland Browns",
        "Pittsburgh Steelers"
        ],
    "South":
        [
        "Houston Texans",
        "Indianapolis Colts",
        "Jacksonville Jaguars",
        "Tennessee Titans"
        ],
    "West":
        [
        "Denver Broncos",
        "Kansas City Chiefs",
        "Oakland Raiders",
        "San Diego Chargers"
        ]
        },
"NFC":{
    "East":
        [
        "Dallas Cowboys",
        "New York Giants",
        "Philadelphia Eagles",
        "Washington Redskins"
        ],
    "North":
        [
        "Chicago Bears",
        "Detroit Lions",
        "Green Bay Packers",
        "Minnesota Vikings"
        ],
    "South":
        [
        "Atlanta Falcons",
        "Carolina Panthers",
        "New Orleans Saints",
        "Tampa Bay Buccaneers"
        ],
    "West":
        [
        "Arizona Cardinals",
        "Los Angeles Rams",
        "San Francisco 49ers",
        "Seattle Seahawks"
        ]
        }
}

# "Arizona Cardinals" in NFC.values()

# query = input("Enter the name of either a conference or team: ")
# if query == "AFC" or query == "NFC":
#     division = input ("What division?: ")

# if query == "AFC":
#     if division == "East":
#         print(conferences["AFC"]["East"])
#     elif division == "North":
#         print(conferences["AFC"]["North"])
#     elif division == "South":
#         print(conferences["AFC"]["South"])
#     elif division == "West":
#         print(conferences["AFC"]["West"])
#
# elif query == "NFC":
#     if division == "East":
#         print(conferences["NFC"]["East"])
#     elif division == "North":
#         print(conferences["NFC"]["North"])
#     elif division == "South":
#         print(conferences["NFC"]["South"])
#     elif division == "West":
#         print(conferences["NFC"]["West"])

query = input("Enter the name of either a conference or team: ")

def function(query_user):
    if query_user == "AFC" or query_user == "NFC":
        division = input("What division?: ")
        if division == "East" or division == "North" or division == "South" or division == "West":
            print(conferences[query_user][division])
        else:
            print("Not a valid option")

    for conference_key in conferences:
        for division_key in conferences[conference_key]:
            for team in conferences[conference_key][division_key]:
                if team == query:
                    print (conference_key, division_key)

    # else:
    #     print("Invalid option")

function(query)
