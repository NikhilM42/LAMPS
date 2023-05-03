import numpy as np
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib.dates import bytespdate2num, num2date
import pandas
from itertools import repeat
import datetime

# Your key here
key = 'TCZL6AVQH6JKQQOM'

if __name__ == "__main__":
    stocklist = ['TSE:RY','TSE:VDY','TSE:BB','TSE:LNR','TSE:MFC','TSE:CM']
    data = []
    
    for stock in stocklist:
        data.append(pullstockData(stock))

    levelarray(data)
    printdatatable(data)
    plotdata(data)

def levelarray(dataval):


def printdatatable(dataval):


def plotdata(dataval):
    plt.title('Intraday Times Series (1 day)')
    plt.show()

def pullStockData(symVal):
    ts = TimeSeries(key,output_format='pandas', indexing_type='date')
    #bb, meta = ts.get_intraday(symbol='TSE:BB',interval='1min',outputsize='full')
    bb, meta = ts.get_daily(symbol=symVal,outputsize='full')

    summarydata = {}
    
    #basedate = '2020-01-'
    yearrange = range(2001,2021,1)
    dayrange = range(1,32,1)
    monthrange = range(1,13,1)

    x=0
    for c in yearrange:
        for b in monthrange:
            for a in dayrange:
                try:
                    sat = datetime.date(c,b,a).weekday()
                    cordate = True
                except ValueError:
                    cordate = False
                            
                if cordate and sat<5 and datetime.date(c,b,a) < datetime.datetime.now().date():
                    x+=len(bb['4. close'].loc[str(datetime.date(c,b,a))])

    newindex = range(0,x,1)

    bbnew = []

    #daily slope
    dmindex = [] #daily slope index range
    dm = [] #daily slope
    dmc = 0 #daily slope quantity counter

    prevval = -1
    msum = 0
    mcount = 0
    mnf = 0
    mpf = 0
    tempm = 0
    prevm = 0
    start=0
    end=0
    xintrcpt = []
    mval = 0
    mpk = 0
    mclifffall=0
    mcliffclimb=0
    mflat=0
    mclimb=0
    mfall=0
    maxclimb=0
    climb = 0

    for c in yearrange:
        for b in monthrange:
            for a in dayrange:
                try:
                    sat = datetime.date(c,b,a).weekday()
                    cordate = True
                except ValueError:
                    cordate = False

                if cordate and sat<5 and datetime.date(c,b,a) < datetime.datetime.now().date():
                    #start = mcount #track start of day index
                    #dm.append(0) #add a new days slope
                    xintrcpt.append(start)
                    for val in bb['4. close'].loc[str(datetime.date(c,b,a))]:
                        if prevval>0:
                            prevm = tempm
                            tempm = val-prevval
                            if (tempm)<0:
                                mnf+=1
                            else:
                                mpf+=1

                            if prevm<0 and tempm>0:
                                mval+=1
                            elif prevm>0 and tempm<0:
                                mpk+=1
                                if climb > maxclimb:
                                    maxclimb = climb
                                climb=0
                            elif prevm==0 and tempm<0:
                                mclifffall+=1
                                if climb > maxclimb:
                                    maxclimb = climb
                                climb=0
                            elif prevm>0 and tempm==0:
                                mcliffclimb+=1
                                climb+=1
                            elif prevm==0 and tempm==0:
                                mflat+=1
                                climb+=1
                            elif prevm>0 and tempm>0:
                                mclimb+=1
                                climb+=1
                            elif prevm<0 and tempm<0:
                                mfall+=1
                                    
                            msum = msum + tempm
                            mcount+=1
                                
                            #dm[dmc]+=(val-prevval)
                                
                        bbnew.append(val)
                        prevval = val
                    #end = mcount #track end of day index
                    #dm[dmc] = dm[dmc]/(end-start) #build the slope for the current day
                    #dmindex.append(list(range(start,end,1))) #build the slope navigation index
                    #dmc+=1 #increment to the next dayrange

    m = msum/mcount #overall slope
##    print("Average slope: ", m,
##          "\n# of Increases: ", mnf,
##          "\n# of Drops: ", mpf,
##          "\n# of Valleys: ", mval,
##          "\n# of Peaks: ",mpk,
##          "\n# of Cliff Falls: ",mclifffall,
##          "\n# of Cliff Climbs: ",mcliffclimb,
##          "\n# of Flats: ",mflat,
##          "\n# of Falls: ",mfall,
##          "\n# of Climbs: ",mclimb,
##          "\nMax Sequence of Climbs: ", maxclimb)

    #bbtrendone = []

    b = 0
    cntr=0
    for val in newindex:
        #b+=(bbnew[cntr] - m*(val))
        b+=bbnew[cntr]
        cntr+=1

    b=(b/cntr-m*(cntr/2))

    smallm = 0
    prevval = 0
    mcount = 0
    for val in range(len(newindex)-100,len(newindex)):
        if prevval>0:
            smallm = smallm + (bbnew[val]-prevval)
            mcount+=1
        prevval = val

    smallm = smallm/mcount

    ##bbtrendtwo = []
    ##cntr=0
    ##dailyb=list(repeat(0, dmc)) #initialize b values list for every day
    ##dmc = 0
    ##for dailyindex in dmindex: #calculate ethrough each days index position
    ##    bcntr = 0
    ##    dailyb[dmc] = 0
    ##    for val in dailyindex:#calculate each days b value
    ##        tempm = dm[dmc]
    ##        tempval = (val-dailyindex[0])
    ##        #dailyb[dmc]+=(bbnew[cntr] - tempm*tempval)
    ##        dailyb[dmc]+=bbnew[cntr]
    ##        cntr+=1
    ##        bcntr+=1
    ##    dailyb[dmc]=(dailyb[dmc]/bcntr)-(tempm*(bcntr/2))
    ##    dmc+=1

    ##dmc = 0
    ##for dailyindex in dmindex: #calculate ethrough each days index position
    ##    for val in dailyindex:
    ##        bbtrendtwo.append(dm[dmc]*(val-xintrcpt[dmc])+dailyb[dmc])
    ##    dmc+=1
    filteredresult = []
    dt = 1
    RC = 40
    alpha = dt/(dt+RC)

    filteredresultTwo = []
    dtTwo = 1
    RCTwo = 240
    alphaTwo = dtTwo/(dtTwo+RCTwo)

    for val in newindex:
        bbtrendone.append(m*val+b)
        if val == 0:
            filteredresult.append(bbnew[val])
            filteredresultTwo.append(bbnew[val])
        else:
            filteredresult.append(alpha*bbnew[val]+(1-alpha)*filteredresult[val-1])
            filteredresultTwo.append(alpha*filteredresult[val]+(1-alpha)*filteredresultTwo[val-1])

    summarydata["Average slope"] = m
    summarydata["# of Increases"] = mnf
    summarydata["# of Drops"] = mpf
    summarydata["# of Valleys"] = mval
    summarydata["# of Peaks"] = mpk
    summarydata["# of Cliff Falls"] = mclifffall
    summarydata["# of Cliff Climbs"] = mcliffclimb
    summarydata["# of Flats"] = mflat
    summarydata["# of Falls"] = mfall
    summarydata["# of Climbs"] = mclimb
    summarydata["Max Sequence of Climbs"] = maxclimb
    summarydata["Main Data"] = bbnew
    summarydata["First Filtered Pass"] = filteredresult
    summarydata["Second Filtered Pass"] = filteredresultTwo
    
    #plt.plot(newindex,bbnew,newindex,filteredresult,newindex,filteredresultTwo)#,newindex,bbtrendone,newindex[0:(len(newindex)-1)],bbtrendtwo)
    return summarydata

