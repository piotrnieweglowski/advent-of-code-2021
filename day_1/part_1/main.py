def check_increasing_depths(depths):
    inc = 0
    last = depths[0]
    for d in depths[1:]:
        if last < d:
            inc += 1
        last = d
    return inc

with open("../input.txt") as f:
    depths = []
    for l in f.readlines():
        depths.append(int(l.replace("\n", "")))

if __name__ == '__main__':
    print(check_increasing_depths(depths))