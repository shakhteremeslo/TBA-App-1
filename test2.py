import requests, json, sys

key = sys.argv[1]
url = "https://www.thebluealliance.com/api/v3/team/frc"
headers = {"X-TBA-Auth-Key":key}

for team in range(1258):
    try:
        content = json.loads(requests.get(url + str(team) + "/robots", headers=headers).text)
        print(content[0]["team_key"][3:7] + "'s robot in " + str(content[0]["year"]) + " was called " + content[0]["robot_name"])
    except:
        pass