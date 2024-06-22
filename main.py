import json

class Meteorite:
    def __init__(self):
        with open('Raw_data.json') as json_data:
            self.data = json.load(json_data)

    def years(self): 
        # Contains duplicates
        years = []

        for i in self.data:
            if "year" not in i.keys():
                print("year key missing for ID : {}".format(i["id"]))
                continue
            years.append(i["year"][:4])

        years.sort()

        # Non-duplicate unique years
        yearSet = list(set(years))
        yearSet.sort()
        
        # Years divided in groups of 10 (except the last group)
        grouping = []

        for i in range(0,len(yearSet)-10,10):
            grouping.append((yearSet[i],yearSet[i+9]))
        grouping.append((yearSet[i+10],yearSet[-1]))

        print(grouping[-1])


if __name__ == "__main__":
    meteors = Meteorite()
    meteors.years()




