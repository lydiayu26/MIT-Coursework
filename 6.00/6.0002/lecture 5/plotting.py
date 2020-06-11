import matplotlib.pyplot as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

##### Plotting one line
#plt.plot(mySamples, myLinear)

####### Plotting many lines
#plt.plot(mySamples, myLinear)
#plt.plot(mySamples, myQuadratic)
#plt.plot(mySamples, myCubic)
#plt.plot(mySamples, myExponential)

###### Plotting on multiple figures
#plt.figure('expo')
#plt.plot(mySamples, myExponential)
#plt.figure('lin')
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.plot(mySamples, myCubic)
#newExpo = []
#for i in range(30):
#    newExpo.append(1.6**i)
#plt.figure('expo')
#plt.plot(mySamples, newExpo)

###### Plotting temperatures and changing xaxis
#months = range(1, 13, 1)
#temps = [28,32,39,48,59,68,75,73,66,54,45,34]
#plt.plot(months, temps)
#
#plt.title('Ave. Temperature in Boston')
#plt.xlabel('Month')
#plt.ylabel(('Degrees F'))
#
#plt.xlim(1, 12)
##
#plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12))
#
#plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12),
#           ('Jan','Feb','Mar','Apr','May','Jun','Jul',\
#             'Aug','Sep','Oct','Nov','Dec'))

##### Plotting multiple lines with labels
months = range(1, 13, 1)
boston = [28,32,39,48,59,68,75,73,66,54,45,34]
plt.plot(months, boston, label = 'Boston')
phoenix = [54,57,61,68,77,86,91,90,84,73,61,54]
plt.plot(months, phoenix, label = 'Phoenix')
plt.legend(loc = 'best') # position it automatically

plt.title('Ave. Temperatures')
plt.xlabel('Month')
plt.ylabel(('Degrees F'))

plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12),
           ('Jan','Feb','Mar','Apr','May','Jun','Jul',\
             'Aug','Sep','Oct','Nov','Dec'))

###### Plotting multiple lines and changing their line style
#months = range(1, 13, 1)           
#boston = [28,32,39,48,59,68,75,73,66,54,45,34]
#plt.plot(months, boston, 'b-', label = 'Boston')
#phoenix = [54,57,61,68,77,86,91,90,84,73,61,54]
#plt.plot(months, phoenix, 'r--', label = 'Phoenix')
#msp = [16,19,34,48,59,70,75,73,64,60,37,21]
#plt.plot(months, msp, 'g.-.', label = 'Minneapolis')
#plt.legend(loc = 'best')
#
#plt.title('Ave. Temperatures')
#plt.xlabel('Month')
#plt.ylabel(('Degrees F'))
#
#plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12),
#           ('Jan','Feb','Mar','Apr','May','Jun',\
#           'Jul','Aug','Sep','Oct','Nov','Dec'))


def getUSPop(fileName):
    inFile = open(fileName, 'r')
    dates, pops = [], []
    for l in inFile:
        line = ''
        for c in l:
            if c in '0123456789 ':
                line += c
        line = line.split(' ')
        dates.append(int(line[0]))
        pops.append(int(line[1][:-1]))
    return dates, pops

#dates, pops = getUSPop('USPopulation.txt')
#plt.plot(dates, pops)
#plt.title('Population in What Is Now U.S\n' +\
#          '(Native Am. Excluded Before 1860)')
#plt.xlabel('Year')
#plt.ylabel('Population')
##plt.semilogy()   




