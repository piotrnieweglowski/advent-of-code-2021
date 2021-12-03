def calculate_chars(input, pos):
    count = { "0": 0, "1": 0 }
    for i in input:
        count[i[pos]] += 1 
    return count

def calculate_params(chars_count):
    if chars_count["0"] > chars_count["1"]: 
        return "0", "1"
    return "1", "0"

def calculate_power_consumption(input):
    gamma = ""
    epsilon = ""
    length = len(input[0])
    for i in range(length):
        count = calculate_chars(input, i)
        g, e = calculate_params(count)
        gamma += g
        epsilon += e
    return int(gamma, 2) * int(epsilon, 2)

with open("../input.txt") as f:
    input = []
    for l in f.readlines():
        input.append(l.replace("\n", ""))

if __name__ == '__main__':
    print(calculate_power_consumption(input))
    