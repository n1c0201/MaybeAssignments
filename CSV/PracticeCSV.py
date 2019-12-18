import numpy as np
import matplotlib.pyplot as plt
import random
import statistics as stat

with open("activity.csv", 'r') as file:
    rawData = file.readlines()

for i in range(len(rawData)):
    rawData[i] = rawData[i].replace('"', '').replace(",", " ").split()
rawData.pop(0)
dateData = {}

for i in rawData:
    dateData["{}:{}".format(i[1], i[2].zfill(4))] = i[0]          #2012-11-30-2300, step value not yet int

dateList = {}
for i in dateData:
    if dateData[i] != "NA":
        if i[:10] not in dateList:
            dateList[i[:10]] = int(dateData[i])
        else:
            dateList[i[:10]] += int(dateData[i])
    else:
        dateList[i[:10]] = 0


plt.bar(dateList.keys(), dateList.values())
plt.show()

stepInterval = {}
for i in dateData:
    if dateData[i] != "NA":
        if i[11:] not in stepInterval:
            stepInterval[i[11:]] = int(dateData[i])
        else:
            stepInterval[i[11:]] += int(dateData[i])

x = np.array(list(stepInterval.keys()))
y = np.array(list(stepInterval.values()))
plt.plot(x, y)
plt.show()

naCount = 0
for i in dateData:
    if dateData[i] == "NA":
        naCount += 1
print("Number of datas that were Not Available: ", naCount)

newDateData = dateData

for i in newDateData:
    if newDateData[i] == "NA":
        newDateData[i] = random.randint(1,50)

newDateList = {}
for i in newDateData:
    if newDateData[i] != "NA":
        if i[:10] not in newDateList:
            newDateList[i[:10]] = int(newDateData[i])
        else:
            newDateList[i[:10]] += int(newDateData[i])
    else:
        newDateList[i[:10]] = 0
newStepInterval = {}

for i in newDateData:
    if newDateData[i] != "NA":
        if i[11:] not in newStepInterval:
            newStepInterval[i[11:]] = int(newDateData[i])
        else:
            newStepInterval[i[11:]] += int(newDateData[i])

plt.bar(newDateList.keys(), newDateList.values())
plt.show()


weekdays = {}
weekends = {}
count = 1
for dates in newDateList:
    if count >= 8:
        count = 1
    if count < 6:
        weekdays[dates] = newDateList[dates]
        count += 1
    elif count >= 6:
        weekends[dates] = newDateList[dates]
        count += 1

weekend_interval = {}

for i in dateData:
    if i[11:] not in weekend_interval:
        weekend_interval[i[11:]] = 0

for dates in newDateData:
    if dates[:10] in weekends:
        weekend_interval[dates[11:]] += int(newDateData[dates])

x2 = np.array(list(weekend_interval.keys()))
y2 = np.array(list(weekend_interval.values()))

plt.plot(x2, y2)
plt.show()

weekday_interval = {}

for i in dateData:
    if i[11:] not in weekday_interval:
        weekday_interval[i[11:]] = 0

for dates in newDateData:
    if dates[:10] in weekdays:
        weekday_interval[dates[11:]] += int(newDateData[dates])

x3 = np.array(list(weekday_interval.keys()))
y3 = np.array(list(weekday_interval.values()))

plt.plot(x3, y3)
plt.show()