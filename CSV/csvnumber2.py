#1

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import statistics
import numpy as np
import datetime

with open("activity.csv") as file:

    #make csv file readable

    dictionary = []
    rows = file.readline().replace('"', "").rstrip().split(",")
    i = 0
    for strr in file.readlines():
        tempArr = strr.rstrip().replace('"', "").split(",")
        newDict = {}
        for j in range(len(rows)):
            newDict[rows[j]] = tempArr[j]
        dictionary.append(newDict)
    
    file.close()

    #make stepsData with calendar {date: steps}

stepsData = {}      # stepsData: {date: int} # time with corresponding steps

for dic in dictionary:
    newInterval = dic['interval'].zfill(4)
    newTime: str = "{date} {hour}:{minute}:00.0000".format(date=dic['date'], hour=newInterval[:-2], minute=newInterval[-2:])
    stepsData[datetime.datetime.strptime(newTime, '%Y-%m-%d %H:%M:%S.%f')] = dic['steps']

    #mean median total

datesList: [str] = []   # list of all of the dates in the file

for i in stepsData.keys():
    if str(i.date()) not in datesList:
        datesList.append(str(i.date()))

timeList: [str] = []

for i in stepsData.keys():
    if str(i.time()) not in timeList:
        timeList.append(str(i.time()))

dayStepsData: dict = {} # dayStepsData: {Date: [steps]} # date with corresponding list of steps

for i in stepsData:
    if str(i.date()) not in dayStepsData.keys():
        dayStepsData[str(i.date())] = []
    if stepsData[i] != "NA":
        dayStepsData[str(i.date())].append(int(stepsData[i]))

stepsTotalDay = [sum(dayStepsData[i]) for i in dayStepsData.keys()]
stepsMean = [statistics.mean(dayStepsData[i]) if len(dayStepsData[i]) > 0 else 0 for i in dayStepsData.keys()]
stepsMedian = [statistics.median(dayStepsData[i]) if len(dayStepsData[i]) > 0 else 0 for i in dayStepsData.keys()]

intervalStepsData: dict = {} # intervalStepsData: {Time: [steps]} # time with corresponding list of steps

for i in stepsData:
    if str(i.time()) not in intervalStepsData.keys():
        intervalStepsData[str(i.time())] = []
    if stepsData[i] != "NA":
        intervalStepsData[str(i.time())].append(int(stepsData[i]))

weekdaysIntervalStepsData: dict = {}
weekendsIntervalStepsData: dict = {}

for i in stepsData:
    if i.strftime("%A") != "Saturday" and i.strftime("%A") != "Sunday":
        if str(i.time()) not in weekdaysIntervalStepsData.keys():
            weekdaysIntervalStepsData[str(i.time())] = []
        if stepsData[i] != "NA":
            weekdaysIntervalStepsData[str(i.time())].append(int(stepsData[i]))
    else:
        if str(i.time()) not in weekendsIntervalStepsData.keys():
            weekendsIntervalStepsData[str(i.time())] = []
        if stepsData[i] != "NA":
            weekendsIntervalStepsData[str(i.time())].append(int(stepsData[i]))

for i in stepsData:
    if str(i.date()) not in dayStepsData.keys():
        dayStepsData[str(i.date())] = []
    if stepsData[i] != "NA":
        dayStepsData[str(i.date())].append(int(stepsData[i]))

newDayStepsData = {}

for i in stepsData:
    if str(i.date()) not in newDayStepsData.keys():
        newDayStepsData[str(i.date())] = []
    if stepsData[i] != "NA":
        newDayStepsData[str(i.date())].append(int(stepsData[i]))
    else:
        newData = statistics.mean(intervalStepsData[str(i.time())]) if len(intervalStepsData[str(i.time())]) > 0 else 0
        newDayStepsData[str(i.date())].append(newData)

newStepsTotalDay = [sum(newDayStepsData[i]) for i in newDayStepsData.keys()]
newStepsMean = [statistics.mean(newDayStepsData[i]) if len(newDayStepsData[i]) > 0 else 0 for i in newDayStepsData.keys()]
newStepsMedian = [statistics.median(newDayStepsData[i]) if len(newDayStepsData[i]) > 0 else 0 for i in newDayStepsData.keys()]

    #init tables

tWidth = [2, 2, 1]
tHeight = [2, 2, 1]

tableFigure = plt.figure(constrained_layout=True)
gridSize = tableFigure.add_gridspec(ncols=3, nrows=3, width_ratios=tWidth, height_ratios=tHeight)


totalPlot = tableFigure.add_subplot(gridSize[0, 0])
meanPlot = tableFigure.add_subplot(gridSize[0, 1])
weekdaysPlot = tableFigure.add_subplot(gridSize[1, 0])
weekendsPlot = tableFigure.add_subplot(gridSize[1, 1])

meanRevisedPlot = tableFigure.add_subplot(gridSize[2, 1])
medianRevisedPlot = tableFigure.add_subplot(gridSize[2, 2])
totalRevisedPlot = tableFigure.add_subplot(gridSize[2, 0])

medianPlot = tableFigure.add_subplot(gridSize[0, 2])
intervalPlot = tableFigure.add_subplot(gridSize[1, 2])


    #table configuration

totalPlot.bar(dayStepsData.keys(), stepsTotalDay)
plt.setp(totalPlot, title="Total steps per day", xticks=np.arange(0,61,5),)
plt.setp(totalPlot.xaxis.get_majorticklabels(), rotation=45, color='g', size='small')

meanPlot.bar(dayStepsData.keys(), stepsMean)
plt.setp(meanPlot, title="Mean plot per day", xticks=np.arange(0,61,5))
plt.setp(meanPlot.xaxis.get_majorticklabels(), rotation=45, color='g', size='small')

medianPlot.bar(dayStepsData.keys(), stepsMedian)
plt.setp(medianPlot, title="Median plot per day", xticks=np.arange(0,61,10))
plt.setp(medianPlot.xaxis.get_majorticklabels(), rotation=90, color='g', size='xx-small')

intervalPlot.plot( [ str(val) for val in intervalStepsData.keys() ] , [ statistics.mean(val) for val in intervalStepsData.values() ] )
plt.setp(intervalPlot, title="Average activity time plot", xticks=np.arange(0,288,12))
plt.setp(intervalPlot.xaxis.get_majorticklabels(), rotation=90, color='g', size='x-small')

weekdaysPlot.plot( [ str(val) for val in weekdaysIntervalStepsData.keys() ] , [ statistics.mean(val) for val in weekdaysIntervalStepsData.values() ] )
plt.setp(weekdaysPlot, title="Average weekdays activity time plot", xticks=np.arange(0,288,12))
plt.setp(weekdaysPlot.xaxis.get_majorticklabels(), rotation=90, color='g', size='x-small')

weekendsPlot.plot( [ str(val) for val in weekendsIntervalStepsData.keys() ] , [ statistics.mean(val) for val in weekendsIntervalStepsData.values() ] )
plt.setp(weekendsPlot, title="Average weekends activity time plot", xticks=np.arange(0,288,12))
plt.setp(weekendsPlot.xaxis.get_majorticklabels(), rotation=90, color='g', size='x-small')

totalRevisedPlot.bar(dayStepsData.keys(), newStepsTotalDay)
plt.setp(totalRevisedPlot, title="Revised total steps per day", xticks=np.arange(0,61,5))
plt.setp(totalRevisedPlot.xaxis.get_majorticklabels(), rotation=45, color='g', size='small')

meanRevisedPlot.bar(dayStepsData.keys(), newStepsMean)
plt.setp(meanRevisedPlot, title="Revised mean plot per day", xticks=np.arange(0,61,5))
plt.setp(meanRevisedPlot.xaxis.get_majorticklabels(), rotation=45, color='g', size='small')

medianRevisedPlot.bar(dayStepsData.keys(), newStepsMedian)
plt.setp(medianRevisedPlot, title="Revised median plot per day", xticks=np.arange(0,61,10))
plt.setp(medianRevisedPlot.xaxis.get_majorticklabels(), rotation=90, color='g', size='xx-small')

plt.show()