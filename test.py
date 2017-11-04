import requests, json, sys

key = sys.argv[1]
url = "https://www.thebluealliance.com/api/v3/team/frc" + input("Which team do you want to choose? ")
headers = {"X-TBA-Auth-Key":key}

content = json.loads(requests.get(url, headers=headers).text)
print(content["country"])