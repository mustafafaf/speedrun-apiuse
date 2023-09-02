import requests
import json


#print python obj as json
def jsonprint(js):
    print(json.dumps(js,indent=4,))

#convert python object to json
def obj_to_json(js):
    return(json.dumps(js,indent=4,sort_keys=True))

parameters={
    "_bulk":"yes",
    "name": (input("enter game name here: "))
}
print(parameters)

response=requests.get("https://www.speedrun.com/api/v1/games", params=parameters)

#gets ids for games similar to smb and puts in dictionary
def getids():
    dict={}

    for i in response.json()["data"]:
        dict[i["names"]["international"]]=i["id"]
    return dict

dict=getids()

jsonprint(dict)