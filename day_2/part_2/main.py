def calculate_position(moves):
    aim = 0
    depth = 0
    horizontal = 0
    for move in moves:
        s = move.split()
        direction = s[0]
        steps = int(s[1])
        if direction == "forward":
            horizontal += steps
            depth += (aim * steps)
            continue
        if direction == "up":
            aim -= steps
            continue
        aim += steps
    return depth, horizontal

with open("../input.txt") as f:
    moves = []
    for l in f.readlines():
        moves.append(l.replace("\n", ""))

if __name__ == '__main__':
    depth, horizontal = calculate_position(moves)
    print(depth * horizontal)
    