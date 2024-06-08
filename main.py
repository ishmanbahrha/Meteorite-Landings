import json

with open('Raw_data.json') as json_data:
  data = json.load(json_data)

# Years 
years = []

for i in data:
    if "year" not in i.keys():
        print("year key missing for ID : {}".format(i["id"]))
        continue
    years.append(i["year"][:4])







