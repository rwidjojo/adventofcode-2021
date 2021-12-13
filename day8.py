with open("data/data8.txt", "r") as file:
    data = file.readlines()

prob1 = [row.replace("\n","").split(" | ")[1] for row in data]
prob2 = [row.replace("\n","").split(" | ") for row in data]

signal_input = [row.split(" ") for row in prob1]
number_mapping = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9"
}

# PROBLEM 1
def count_occurence(list_of_signals, idx):
    result = [
        list(filter(lambda x: len(x) == idx, row))
        for row in list_of_signals
    ]
    return sum(len(row) for row in result)

print(sum(count_occurence(signal_input, x) for x in [2,3,4,7]))

# PROBLEM 2
def convert_output_to_number(output, final_mapping):
    result = ""
    for guess in output.split(" "):
        data = "".join(sorted(final_mapping[letter] for letter in list(guess)))
        result += number_mapping[data]
    return int(result)

def generate_final_mapping(original_input):
    unique_signal = list(filter(lambda x: len(x) in [2,3,4,7], original_input.split(" ")))
    
    unique_signal_input = "".join(unique_signal)
    
    unique_signal_dict = {
        letter: unique_signal_input.count(letter)
        for letter in set(list(unique_signal_input))
    }
    
    # generate which letter in the input should map to original lamp
    final_mapping = {}
    for letter, occurence in unique_signal_dict.items():
        if occurence == 4:
            if original_input.count(letter) == 8:
                final_mapping[letter] = "c"
            else:
                final_mapping[letter] = "f"
        elif occurence == 1:
            if original_input.count(letter) == 7:
                final_mapping[letter] = "g"
            else:
                final_mapping[letter] = "e"
        else:
            if original_input.count(letter) == 6:
                final_mapping[letter] = "b"
            elif original_input.count(letter) == 7:
                final_mapping[letter] = "d"
            else:
                final_mapping[letter] = "a"
    
    return final_mapping

answer = 0
for row in prob2:
    x, y = row
    z = generate_final_mapping(x)
    answer += convert_output_to_number(y, z)

print(answer)