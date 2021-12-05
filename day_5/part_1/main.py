points = {}
with open("../input.txt") as f:
    for l in f.readlines():
        left, right = l.replace(" ", "").replace("\n", "").split("->")
        x1, y1 = (int(i) for i in left.split(","))
        x2, y2 = (int(i) for i in right.split(","))
        if x1 == x2:
            for p in range(min(y1, y2), max(y1, y2) + 1):
                k = f"{x1},{p}"
                if not k in points:
                    points[k] = 0
                points[k] += 1
        if y1 == y2:
            for p in range(min(x1, x2), max(x1, x2) + 1):
                k = f"{p},{y1}"
                if not k in points:
                    points[k] = 0
                points[k] += 1

print(len(list(v for v in points.values() if v > 1)))