import json

json_data = object()

with open('accessPoints.json') as f:
        json_data = json.load(f)
        
        x = 1

        for i in json_data['accessPoints']:
            old = i["name"]
            i["name"] = "AP{}".format(x)
            new = i["name"]
            print("old: {} - new: {}".format(old, new))
            x = x + 1

with open('accessPoints-resequenced.json', 'w') as outfile:
    json.dump(json_data, outfile)
