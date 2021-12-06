with open("../input.txt") as file:
    fish = list((int(f) for f in file.readline().split(",")))
    days = 80
    for i in range(1, days+1):
        new_fish = []
        children = []
        for f in fish:
            if f == 0:
                children.append(8)
            new_fish.append(f-1 if f > 0 else 6)
        fish = new_fish + children
    print(len(fish))