"""Date class for organizing dates"""
class Date(object):
    #constructor
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
    #print method
    def printDate(self):
        print(str(self.month) + "/" + str(self.day) + "/" + str(self.year))

"""String version of Dates for easier input"""
class StringDate(object):
    #constructor
    def __init__(self, string):
        self.date = string
    #returns Date class from self
    def toDate(self):
        list = self.date.split("/")
        return Date(list[0], list[1], list[2])

"""Method to return a list of sorted Dates"""
def sortDates(dates):
    for i in range(len(dates)-1):
        j = i + 1
        while j < len(dates):
            if dates[i].year > dates[j].year:
                temp = dates[i]
                dates[i] = dates[j]
                dates[j] = temp
            elif dates[i].year == dates[j].year:
                if dates[i].month > dates[j].month:
                    temp = dates[i]
                    dates[i] = dates[j]
                    dates[j] = temp
                elif dates[i].month == dates[j].month:
                    if dates[i].day > dates[j].day:
                        temp = dates[i]
                        dates[i] = dates[j]
                        dates[j] = temp
            j += 1
    return dates;

"""Scripting"""
date1 = StringDate("4/1/2016")
date2 = StringDate("1/10/2016")
date3 = StringDate("12/12/2016")
date4 = StringDate("10/4/2015")
date5 = StringDate("9/1/2000")
date6 = StringDate("4/2/2016")
date7 = StringDate("5/1/2016")

dates = [date1.toDate(), date2.toDate(), date3.toDate(), date4.toDate(), date5.toDate(), date6.toDate(), date7.toDate()]
dates = sortDates(dates)

print("Sorted Dates:")
for date in dates:
    date.printDate()
