import numpy as np
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib.dates import bytespdate2num, num2date
import pandas
from itertools import repeat
import datetime
import time
import sys

# Your key here
loginkey = 'TCZL6AVQH6JKQQOM'

def printdatatable(dataval,keylist):
    etitlelist = ["Stock",
                 "Average slope",
                 "# of Increases",
                 "# of Drops",
                 "# of Valleys",
                 "# of Peaks",
                 "# of Cliff Falls",
                 "# of Cliff Climbs",
                 "# of Flats",
                 "# of Falls",
                 "# of Climbs",
                 "Max Sequence of Climbs"]
  #               "Main Data"]

    titlelist = ["Stock",
                 "AvgM",
                 "Incrs",
                 "Drops",
                 "Vllys",
                 "Peaks",
                 "CFall",
                 "CClmb",
                 "Flats",
                 "Falls",
                 "Climb",
                 "MSoCl"] 
    
    title = ""
    
    for val in titlelist:
        title = title + val + "\t" 

    title = title[:-1]
    print("\n",title)
    
    for key in keylist:
        entry = ""
        for val in titlelist:
            entry = entry + str(dataval[key][val])[:8] + "\t"
        print(entry)

def levelarray(dataval,keylist):
    maxlen = 0
    for val in keylist:
       newlen = len(dataval[val]["Main Data"])
       if newlen>maxlen:
           maxlen = newlen
    addlen = 0
    for val in keylist:
        addlen = maxlen-len(dataval[val]["Main Data"])
        dataval[val]["Main Data"] = [0]*addlen + dataval[val]["Main Data"]
        addlen = maxlen-len(dataval[val]["First Filtered Pass"])
        dataval[val]["First Filtered Pass"] = [0]*addlen + dataval[val]["First Filtered Pass"]
        addlen = maxlen-len(dataval[val]["Second Filtered Pass"])
        dataval[val]["Second Filtered Pass"] = [0]*addlen + dataval[val]["Second Filtered Pass"]
    return dataval

def plotdata(dataval,keylist):
    newindex = range(0,len(dataval[keylist[0]]["Main Data"]))
    for val in keylist:
        #print(val, ", ", len(newindex), ", " , len(dataval[val]["Main Data"]))
        plt.plot(newindex,dataval[val]["Main Data"],label=("Main Data - " + val))
        #print(len(dataval[val]["First Filtered Pass"]))
        #plt.plot(newindex,dataval[val]["First Filtered Pass"],label=("1st Pass - " + val))
        #print(len(dataval[val]["Second Filtered Pass"]))
        #plt.plot(newindex,dataval[val]["Second Filtered Pass"],label=("2nd Pass - " + val))

    plt.legend(loc="upper left")    
    plt.title('Stock Data 2001 till now')
    plt.show()

def pullAllStockData(symVal):
    ts = TimeSeries(loginkey,output_format='pandas', indexing_type='date')
    #bb, meta = ts.get_intraday(symbol=symVal,interval='1min',outputsize='full')
    bb, meta = ts.get_daily(symbol=symVal,outputsize='full')
    bb.to_csv('Output' + symVal.split(":")[1] + '.csv')
    
    summarydata = {}
    
    #basedate = '2020-01-'
    yearrange = range(1970,2021,1)
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
                                
                        bbnew.append(val)
                        prevval = val


    m = msum/mcount

    b = 0
    cntr=0
    for val in newindex:
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

    summarydata["Stock"] = symVal
    summarydata["AvgM"] = format(m,'.5g')
    summarydata["Incrs"] = mnf
    summarydata["Drops"] = mpf
    summarydata["Vllys"] = mval
    summarydata["Peaks"] = mpk
    summarydata["CFall"] = mclifffall
    summarydata["CClmb"] = mcliffclimb
    summarydata["Flats"] = mflat
    summarydata["Falls"] = mfall
    summarydata["Climb"] = mclimb
    summarydata["MSoCl"] = maxclimb
    summarydata["Main Data"] = bbnew
    
    #plt.plot(newindex,bbnew,newindex,filteredresult,newindex,filteredresultTwo)#,newindex,bbtrendone,newindex[0:(len(newindex)-1)],bbtrendtwo)
    return summarydata

if __name__ == "__main__":
    #stocklist = ['TSE:RY','TSE:BMO','TSE:CM','TSE:BNS','TSE:TD','TSE:MFC','TSE:VDY']
    stocklist = ['TSE:CM']
    data = {}
    cntr = 0
    maxcount = len(stocklist)
    progress = "Progress:= " + format(100.00*(cntr/maxcount),'.2g') + "%"
    print(progress,end="\r")
    
    for stock in stocklist:
        if cntr>0:
            time.sleep(15)
        data[stock] = pullAllStockData(stock)
        cntr+=1
        progress = "Progress:= " + format(100.00*(cntr/maxcount),'.2g') + "%"
        sys.stdout.flush()
        print(progress,end="\r")

    printdatatable(data,stocklist)
    data = levelarray(data,stocklist)
    plotdata(data,stocklist)
