import json

class Meteorite:
    def __init__(self):
        with open('Raw_data.json') as json_data:
            self.data = json.load(json_data)

    def years(self): 
        # Contains duplicates
        self.yearsAll = []

        for i in self.data:
            if "year" not in i.keys():
                print("year key missing for ID : {}".format(i["id"]))
                continue
            self.yearsAll.append(i["year"][:4])

        self.yearsAll.sort()

        # Non-duplicate unique years
        yearSet = list(set(self.yearsAll))
        yearSet.sort()
        
        # Years divided in groups of 10 (except the last group)
        grouping = []

        for i in range(0,len(yearSet)-10,10):
            grouping.append((yearSet[i],yearSet[i+9]))
        grouping.append((yearSet[i+10],yearSet[-1]))

    def meteors(self):
        metCount = {}
        print(self.years.yearsAll)
        # for i in self.yearsAll:
        #     metCount[i] = self.yearsAll.count(i)



if __name__ == "__main__":
    meteors = Meteorite()
    meteors.meteors()




