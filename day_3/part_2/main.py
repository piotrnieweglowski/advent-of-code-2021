def calculate_chars(input, pos):
    count = { "0": 0, "1": 0 }
    for i in input:
        count[i[pos]] += 1 
    return count

def calculate_params(chars_count, most_common, default):
    if chars_count["0"] == chars_count["1"]: 
        return default
    if chars_count["0"] > chars_count["1"]: 
        return "0" if most_common else "1"
    return "1" if most_common else "0"

def filter_input(input, pos, char):
    new_input = []
    for i in input:
        if i[pos] == char:
            new_input.append(i)
    return new_input

def calculate_oxygen(input):
    oxygen = input.copy()
    index = 0
    while len(oxygen) != 1:
        count = calculate_chars(oxygen, index)
        c = calculate_params(count, True, "1")
        oxygen = filter_input(oxygen, index, c)
        index += 1
    return oxygen[0]

def calculate_co2(input):
    co2 = input.copy()
    index = 0
    while len(co2) != 1:
        count = calculate_chars(co2, index)
        c = calculate_params(count, False, "0")
        co2 = filter_input(co2, index, c)
        index += 1
    return co2[0]

def calculate_life_support_rating(input):
    oxygen = calculate_oxygen(input)
    co2 = calculate_co2(input)
    return int(oxygen, 2) * int(co2, 2)

with open("../input.txt") as f:
    input = []
    for l in f.readlines():
        input.append(l.replace("\n", ""))

if __name__ == '__main__':
    print(calculate_life_support_rating(input))
    