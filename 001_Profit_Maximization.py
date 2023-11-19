'''
    First example
    input: 
    "14 5 1 6 3 2 5 6 1 3 6 2 5 5 10"

    Number of predicted days = 14
    Sequence of predicted share prices = [5,1,6,3,2,5,6,1,3,6,2,5,5,10]
    
    output: 9
    
    ---------------------------------------------------------------------
    Second Example
    input: 
    "8 100 10 12 5 6 14 5 6"
    
    Number of predicted days = 8

    A sequence of predicted share prices = [100, 10, 12, 5, 6, 14, 5, 6]
    Output: 9
     
'''

import json

INPUT_FILE = "001_input.json"
OUTPUT_FILE = "001_output.json"

results = []

with open(INPUT_FILE, 'r') as json_file:
    data = json.load(json_file)
    
for time_interval in data['inputs']:
    day = list(map(int, time_interval.split()))
    number_of_days = day.pop(0)
    
    lowest_value = min(day)
    lowest_index = day.index(lowest_value)
    
    days_after_lowest = [d for d in day if day.index(d) >= lowest_index]
    high_value = max(days_after_lowest)

    results.append(high_value-lowest_value)
    
    results_dict = {
        "answer":results
    }

with open(OUTPUT_FILE, 'w') as json_file:
    json.dump(results_dict, json_file, indent=4)
