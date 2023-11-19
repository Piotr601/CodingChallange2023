import json

INPUT_FILE = "003_input.json"
OUTPUT_FILE = "003_output.json"

results = []

def portfolio_operation(file):
    na, nb, maxsum = list(map(int, file[0].split()))
    stack_a = list(map(int, file[1].split()))
    stack_b = list(map(int, file[2].split()))
    
    current_sum, current_int = 0, 0
        
    while True:
        len_a = len(stack_a)
        len_b = len(stack_b)
        
        if len_a and len_b:
            if stack_a[0] > stack_b[0]:
                current_int += 1
                current_sum += stack_b.pop(0)
                
            elif stack_a[0] <= stack_b[0]:
                current_int += 1
                current_sum += stack_a.pop(0)
                
        elif len_a:
            current_int += 1
            current_sum += stack_a.pop(0)

        elif len_b:
            current_int += 1
            current_sum += stack_b.pop(0)
        
        if not len_a and not len_b:
            current_int += 1
            break
        
        if current_sum > maxsum:
            break
        
    return current_int - 1

with open(INPUT_FILE, 'r') as json_file:
    data = json.load(json_file)
    
for item in data['inputs']:
    results.append(portfolio_operation(item))
    
results_dict = {
    "answer":results
}
    
with open(OUTPUT_FILE, 'w') as json_file:
    json.dump(results_dict, json_file, indent=4)

