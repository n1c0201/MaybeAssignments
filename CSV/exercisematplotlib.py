import matplotlib.pyplot as plt
import csv
import statistics
csv_file = open('activity.csv')
csv_reader = csv.reader(csv_file, delimiter= ',')

#calculating total steps per day
linecount = 0
days = {}
for row in csv_reader:
    if linecount == 0:
        linecount += 1
    else:
        text = row[0]
        day = row[1]
        if day in days:
            if text == "NA":
                continue
            else:
                days[day].append(int(text))
        else:
            if text == "NA":
                days[day] = [0]
            else:
                days[day] = [int(text)]
print(days)

#total
totalDays = {}
for day in days:
    total = 0
    for steps in days[day]:
        total += steps
    totalDays[day] = total
    
#histogram
plt.bar(totalDays.keys(), totalDays.values(), 1.0)
plt.xticks(rotation=90)
plt.show()

#mean and median
for day in days:
    print(day + ":")
    print(statistics.mean(days[day]))
    print(statistics.median(sorted(days[day])))

#timeseriesplot
intervals = {}
for i in days:
    for j in days[i]:
        intervals[i] += j
print(intervals)
