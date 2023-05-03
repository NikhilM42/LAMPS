import pandas as pd
import requests
import plotly.express as px

from function.function import function

#word scraper
    #where the hell do I pull this from?
    #use beautiful soup???

#def addevent(eventlist):
    #event id
    #default value of 1

#remove event
    #event id

def pulldata():
    return 0

def getData():
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': '9606148177e148b49043fd12fa68299b'
    }

    r = requests.post('https://analyticsapi.tmxanalytics.com/v1/authn', headers = headers)

    print(r.json())
    
def main():
    population_count = 40
    generation_limit = 1000
    population: list[function] = []
    population_output = []
    
    # generate population of new functions
    for citizen_index in range(population_count):
        population.append(function())

    dataFrame = pd.read_csv("DATA_CM.csv")
    
    for citizen_index in range(population_count):
        citizen: function = population[citizen_index]
        population_output.append([])
        for index, row in dataFrame.iterrows():
            input_val: int = row['TSE:CM(open)']
            result = citizen.calculate_function(input_val)
            population_output[citizen_index].append(result)
    
    figure = px.line(population_output, x = 'Number', y = 'Result')
    figure.show()

if __name__ == "__main__":
    main()
