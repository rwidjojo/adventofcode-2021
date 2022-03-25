from collections import defaultdict

with open("data/data14.txt", "r") as file:
    data = file.read()


word, mapping = data.split("\n\n")
rules = {row.split(" -> ")[0]: row.split(" -> ")[1] for row in mapping.split("\n")}
pairs = ["".join(pair) for pair in zip(word, word[1:])]

letters_count, pairs_count = defaultdict(int), defaultdict(int)

for letter in word:
    letters_count[letter] += 1

for pair in rules:
    pairs_count[pair] += pairs.count(pair)


def get_next_state(letters_state, pairs_state):

    new_letters_state = letters_state.copy()
    new_pairs_state = defaultdict(int)

    for key, val in pairs_state.items():
        new_letters_state[rules[key]] += val
        new_pairs_state[key[0] + rules[key]] += val
        new_pairs_state[rules[key] + key[1]] += val

    return new_letters_state, new_pairs_state


def get_answer(original_letters_state, original_pairs_state, step=10):
    current_ls = original_letters_state
    current_ps = original_pairs_state
    for i in range(step):
        current_ls, current_ps = get_next_state(current_ls, current_ps)

    return max(current_ls.values()) - min(current_ls.values())


print(get_answer(letters_count, pairs_count, 10))
print(get_answer(letters_count, pairs_count, 40))
