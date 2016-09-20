import json
import operator

with open('data.json') as data_file:
    data = json.load(data_file)


def calculateHighest(userList):
    max = 0
    current = 0
    maxitem = None
    for item in userList:
        current = int(float(item["Day-1"])) + int(float(item["Day-2"])) + int(float(item["Day-3"]))
        if current >= max:
            max = current
            current = 0
            maxitem = item
        else:
            pass
    return ({"name": maxitem["Name"], "max": max})


def descendingAverage(userList):
    max = 0
    current = 0
    maxitem = []
    for item in userList:
        current = int(float(item["Day-1"])) + int(float(item["Day-2"])) + int(float(item["Day-3"])) / 3
        maxitem.append({"name": item["Name"], "average": current})
        maxitem.sort(key=operator.itemgetter('average'))
    return (maxitem)


def returnRange(userList, max, min):
    max = 0
    current = 0
    maxitem = None
    for item in userList:
        current = int(float(item["Day-1"])) + int(float(item["Day-2"])) + int(float(item["Day-3"]))
        if current >= min and current <= max:
            maxitem.append({"name": item["Name"], "total": current})
        else:
            maxitem = None
    return (maxitem)


print calculateHighest(data["Users"]["User"])
print descendingAverage(data["Users"]["User"])
print returnRange(data["Users"]["User"], 20, 40)