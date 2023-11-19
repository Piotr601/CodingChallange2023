import json

INPUT_FILE = "002_input.json"
OUTPUT_FILE = "002_output.json"

results = []

def longest_palindrome(files):
    help_length = 0
    palindrom_length = 0

    letters = list(files.replace(' ',''))
    letters.sort()

    if len(files) == 1:
        return 1

    for char in set(letters):
        c = letters.count(char)
        
        if c % 2 == 0:
            palindrom_length += c
            c = 0
        elif c % 2 != 0 and c > 1:
            while c > 1:
                palindrom_length += 2
                c -= 2
        if c % 2 != 0 and c == 1:
            help_length = 1
    return palindrom_length + help_length

with open(INPUT_FILE, 'r') as json_file:
    data = json.load(json_file)
    
for item in data['inputs']:

    results.append(longest_palindrome(item))
    
results_dict = {
    "answer":results
}
    
with open(OUTPUT_FILE, 'w') as json_file:
    json.dump(results_dict, json_file, indent=4)

