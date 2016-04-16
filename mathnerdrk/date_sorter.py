#yes, I know there are classes and I'll create a class for date later on to make things easier
date1 = "4/1/2016"
date2 = "1/10/2016"
date3 = "12/12/2016"
date4 = "10/4/2015"
date5 = "9/1/2000"
date6 = "4/2/2016"
date7 = "5/1/2016"

dates = [date1, date2, date3, date4, date5, date6, date7]

def toArray(date):
    list = []
    if date[1] == '/':
        list.append(int(date[0]))
        if date[3] == '/':
            list.append(int(date[2]))
        else:
            list.append(int(date[2:4]))
    else:
        list.append(int(date[0:2]))
        if date[4] == '/':
            list.append(int(date[3]))
        else:
            list.append(int(date[3:5]))

    list.append(int(date[len(date)-4:]))

    return list


def sortDates(dates):
    for i in range(len(dates)-1):
        j = i + 1
        while j < len(dates):
            if dates[i][2] > dates[j][2]:
                temp = dates[i]
                dates[i] = dates[j]
                dates[j] = temp
            elif dates[i][2] == dates[j][2]:
                if dates[i][0] > dates[j][0]:
                    temp = dates[i]
                    dates[i] = dates[j]
                    dates[j] = temp
                elif dates[i][0] == dates[j][0]:
                    if dates[i][1] > dates[j][1]:
                        temp = dates[i]
                        dates[i] = dates[j]
                        dates[j] = temp
            j += 1
    return dates;

arrayed = []
for date in dates:
    arrayed.append(toArray(date))
print(sortDates(arrayed))
