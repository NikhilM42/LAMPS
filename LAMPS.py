import math
from random import seed
from random import random
import pandas as pd

from .functions import function

#word scraper
    #where the hell do I pull this from?
    #use beautiful soup???

#def addevent(eventlist):
    #event id
    #default value of 1

#remove event
    #event id

def pulldata():
    
def main():
    popCount = 40
    generationlimit = 1000
    population = []
    populationoutput = []
    
    for citizen in range(popCount):
        population.append(generatefunction())

    data = pd.read_csv("DATA_CM.csv")
    
    for citizen in range(popCount):
        for datapoint in data:
            result = calculatefunction(citizen,datapoint['Number'])

if __name__ == "__main__":
    main()

