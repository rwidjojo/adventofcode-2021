with open("data/data10.txt", "r") as file:
    data = file.read().split("\n")
    
# MAPPING DATA
mapping = { "(": ")", "[": "]", "{": "}", "<": ">"}
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
complete_score = {")": 1, "]": 2, "}": 3, ">": 4}

# FUNCTIONS
def remove_parentheses(word):
    return word.replace("()", "").replace("<>", "").replace("{}", "").replace("[]", "")

def find_leftmost(final_word):
    position = list(map(lambda x: final_word.find(x), score.keys()))
    plus_only = [item for item in position if item > 0]
    
    if len(plus_only) == 0:
        return None
    else:
        return min(plus_only)

def solve(strings):
    current = strings
    while True:
        new = remove_parentheses(current)
        if new == current:
            break
        current = new

    return new
  
# PROBLEM 1
total_1 = 0
clean_input = []
for sample in data:
    trimmed = solve(sample)
    violation_index = find_leftmost(trimmed)
    if violation_index:
        total_1 += score[trimmed[violation_index]]
    else:
        clean_input.append(trimmed)
print(total_1)

# PROBLEM 2
autocompletes = []
for row in clean_input:
    current_score = 0
    for item in list(row)[::-1]:
        current_score = 5 * current_score + complete_score[mapping[item]]
    autocompletes.append(current_score)

total_2 = sorted(autocompletes)[(len(autocompletes) - 1)//2]
print(total_2)
