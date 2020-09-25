# Write out all your comments first


########### Read in Data ###########
# Open file
filename = input("Enter the name of the data file: ")
infile = open(filename, "r")

# print(infile.read())

# Read lines from file
datalist = []

# get data from line
for line in infile:
    date, h, l, r = (line.split(','))
    lowtemp = int(l)
    hightemp = int(h)
    rainfall = float(r)

    m, d, y = date.split('/')
    month = int(m)
    day = int(d)
    year = int(y)

    # put data into list
    datalist.append([day, month, year, lowtemp, hightemp, rainfall])

# close file
infile.close()
########### analyze data ###########
# get date
month = int(input("Enter the month you're interested in: "))
day = int(input("Enter the day you are interested in: "))

gooddata = []

for singleday in datalist:
    if(singleday[0] == day) and (singleday[1] == month):
        gooddata.append([singleday[2], singleday[3], singleday[4], singleday[5]])

# perform analysis
minsofar = 120
maxsofar = -100
numgooddates = 0
sumofmin = 0
sumofmax = 0

for singleday in gooddata:
    numgooddates += 1
    sumofmin += singleday[1]
    sumofmax += singleday[2]

    if singleday[1] < minsofar:
        minsofar = singleday[1]
    if singleday[2] > maxsofar:
        maxsofar = singleday[2]

avglow = sumofmin / numgooddates
avghigh = sumofmax / numgooddates



########### present results ###########


















































