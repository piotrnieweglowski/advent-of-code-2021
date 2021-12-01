class SlidingWindow:
    def __init__(self, list, window_size = 3):
        self.list = list
        self.window_size = window_size

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if (self.index + self.window_size) > len(self.list):
            raise StopIteration

        start = self.index
        stop = self.window_size + self.index
        result = self.list[start:stop]
        self.index += 1
        return result

def group_depths(depths):
    grouped = []
    sliding_window = SlidingWindow(depths)
    for d in sliding_window:
        grouped.append(sum(d))
    return grouped


def check_increasing_depths(depths):
    groupped_depths = group_depths(depths)
    inc = 0
    last = groupped_depths[0]
    for d in groupped_depths[1:]:
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