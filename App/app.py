import json 
import requests
import shutil
import time

""" print("title")
title = input()
#https://api.mangadex.org/docs.html

response = requests.get("https://api.mangadex.org/manga?title=" + title)
if response.status_code == 200:
    parsed = json.loads(response.text)
    
    for titleName in parsed['data']:
        print(titleName['attributes']['title'])
    
    print("Which/One?")
    sel = input()


    #print(json.dumps(parsed, indent=4, sort_keys=True))
    mangaS = parsed['data'][ int(sel)-1  ]
    mID = mangaS['id']
    print(mID)
    print("chapter? ")
    chapter = input()

    #manga feed
    response = requests.get("https://api.mangadex.org/manga/" + mID + "/feed?limit=500&locales[]=en")
    parsed = json.loads(response.text)
    for x in parsed['results']:
        if x['data']['attributes']['chapter'] == chapter:
            chID = x['data']['id']
            hashID = x['data']['attributes']['hash']
            chpData = x['data']['attributes']['data']
            srvRe = requests.get("https://api.mangadex.org/at-home/server/" + chID) 
            srvRePar = json.loads(srvRe.text)  
            index=0
            for image in chpData:
                imgURL = srvRePar['baseUrl'] + "/data/" + hashID + "/" + image
                print(imgURL)
                response = requests.get(imgURL, stream=True)
                if response.status_code == 200:
                    with open('images/'+str(index)+'.png', 'wb') as out_file: #if you don't have an images directory get owned
                        shutil.copyfileobj(response.raw, out_file)
                    del response
                index += 1
                time.sleep(3) #don't be mean
            
            exit()
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    
else:
    print("ERROR GETTING REQUEST") """


def titleSearch(title):
    response = requests.get("https://api.mangadex.org/manga?title=" + title)
    if response.status_code == 200:
        parsed = json.loads(response.text)
        return parsed

def idLoad(mID):
    response = requests.get("https://api.mangadex.org/manga/" + mID + "/feed?limit=500&locales[]=en")
    parsed = json.loads(response.text)
    return parsed
