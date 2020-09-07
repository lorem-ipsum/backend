import json

celebrities = set()

with open("results2.json", "r") as f:
    data = f.read()
    obj = json.loads(data)
    for movie in obj['movies']:
        newcls = movie['celebrities']
        for newcl in newcls:
            celebrities.add(newcl)

for c in celebrities:
    print('https://douban.com/movie/celebrity/'+c)
