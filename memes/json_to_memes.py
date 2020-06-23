import json
import urllib.request

with open('physics_post.json') as json_file:
    data = json.load(json_file)
    for i, d in enumerate(data):
        urllib.request.urlretrieve(d['download_link'], './memes/'+str(i)+'_'+d['points']+".jpg")