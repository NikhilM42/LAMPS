import time
import pandas as pd
import requests
import matplotlib.pyplot as plt
import multiprocessing as mp
from multiprocessing.pool import AsyncResult, Pool

from function.function import function

population: list[function] = []
population_with_results: list[function] = []
counter: int = 0

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

# calculate function deviation score
def calculate_deviation_score(data_set: pd.Series, function_result: list[float]):
    deviation_score = 0
    # calculate the differences between the function result and the data set
    result = data_set.subtract(function_result)
    # calculate the average of the results
    deviation_score = result.mean()
    return deviation_score

def store_result_in_citizen(result):
    global counter
    global population_with_results
    global population

    if len(result[1]) > 0:
        target_index: int = result[0]
        population[target_index].result = result[1]
        population_with_results.append(population[target_index])
    counter += 1

def error_callback(error):
    # print(error)
    global counter
    counter += 1

def calculate_for_current_generation(generation_index: int, current_generation: list[function], point_count: int):
    print('Calculating generation '+ str(generation_index + 1) + '...')
    # create a process pool of 8 processes
    pool: Pool = mp.Pool(processes=8)
    global counter
    counter = 0

    for citizen_index in range(len(current_generation)):
        citizen = current_generation[citizen_index]
        # run citizen.calculate_function() in pool
        pool.apply_async(function.calculate, (citizen, point_count, citizen_index), callback=store_result_in_citizen, error_callback=error_callback)
    
    subcounter: int = 0
    prevcounter: int = 0
    while counter < len(population) and subcounter < 10:
        print(f'Waiting...{counter}', end='\r')
        time.sleep(1)
        if counter == prevcounter:
            subcounter += 1
        else:
            subcounter = 0
        prevcounter = counter
    
    print()
    time.sleep(2)
    pool.close()
    pool.terminate()
    print('Done calculating.') 

def main():
    global counter
    global population
    global population_with_results  
    population_count = 100
    generation_limit = 100
    population_output = []

    # generate population of new functions
    for citizen_index in range(population_count):
        population.append(function(10))

    # read data from csv
    data_frame = pd.read_csv("DATA_CM.csv")
    target_function = data_frame['TSE:CM(open)']
    target_function.plot()
    plt.show()

    target_function.plot()

    for generation_index in range(generation_limit):
        calculate_for_current_generation(generation_index, population, data_frame['Number'].count())

        print('Calculate deviation score for each citizen in current population...')
        deviation_score_list: list[dict] = []
        for citizen_index in range(len(population_with_results)):
            if len(population_with_results[citizen_index].result) == 0:
                continue
            try:
                result = calculate_deviation_score(target_function, population_with_results[citizen_index].result)
                deviation_score_list.append({
                    "score": result,
                    "index": citizen_index
                })
            except:
                deviation_score_list.append({
                    "score": 10000,
                    "index": citizen_index
                })
                continue

        # sort deviation score list by score, lower is better
        deviation_score_list = sorted(deviation_score_list, key=lambda x: x['score'], reverse=True)

        print('Reviewing population...')
        # loop through the sorted list of deviation scores
        for index in range(population_count):
            if index >= len(deviation_score_list):
                population_with_results.append(function(25))
                continue
            citizen_index = deviation_score_list[index]['index']
            # replace the last 1/3 of the population with new functions
            if index > (population_count / 3) * 1:
                population_with_results[citizen_index] = function()
            # mutate the middle 1/3 of the populations existing functions
            elif index > (population_count / 3):
                population_with_results[citizen_index].mutate_function()
        
        # replace population with population_with_results
        population[:] = population_with_results
        population_with_results = []

    print('Plotting results...')
    # plot the results
    for citizen_index in range(len(population)):
        citizen = population[citizen_index]
        if(len(citizen.result) == 0):
            continue
        # covert result of population at citizen_index to pandas series
        try:
            result_to_plot = pd.Series(population[citizen_index].result)
            result_to_plot.plot()
        except:
            continue
    
    plt.show()

if __name__ == "__main__":
    main()
