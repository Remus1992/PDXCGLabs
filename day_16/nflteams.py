# https://api.fantasydata.net/v3/nfl/scores/{format}/AreAnyGamesInProgress

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '3c5be3545ff640dabc2576283277de5c',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.fantasydata.net')
    conn.request("GET", "/v3/nfl/scores/{format}/AreAnyGamesInProgress?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################


# Opening story dialogue
def start_dialogue():
    print("You are a fourth grade student standing in your Elementary School Hallway during recess.\n")
    print("Just before you were released for recess, your teacher announced that the class gerbil\n")
    print("had gone missing. She was extremely upset by this and threatened the class with detention\n")
    print("for the rest of the week if no one came forward to confess. The bell rang before anyone\n")
    print("could speak, so everyone ran out to the playground. You joined them in the initial sprint\n")
    print("but as you ran out you noticed that no one else seemed to take the situation seriously,\n")
    print("so you take it upon yourself to solve this untimely crime. You need to find out who\n")
    print("who committed the crime, why he or she did it, and bring that information to your teacher\n")
    print("in the classroom by the end of recess. If you fail, everyone in the class will get detention.\n")
    print("If you succeed, only the guilty party will get detention. If you do extremely well, everyone\n")
    print("will get a pizza party (with the exception of the guilty party).")
    input("\n\n\n[PRESS ANY KEY]")"
