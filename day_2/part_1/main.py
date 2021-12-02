def calculate_position(moves):
    depth = 0
    horizontal = 0
    for move in moves:
        s = move.split()
        direction = s[0]
        steps = int(s[1])
        if direction == "forward":
            horizontal += steps
            continue
        if direction == "up":
            depth -= steps
            continue
        depth += steps
    return depth, horizontal

with open("../input.txt") as f:
    moves = []
    for l in f.readlines():
        moves.append(l.replace("\n", ""))

if __name__ == '__main__':
    depth, horizontal = calculate_position(moves)
    print(depth * horizontal)
    