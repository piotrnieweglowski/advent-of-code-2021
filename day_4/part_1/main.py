class Point:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.is_marked = False

class Board:
    def __init__(self):
        self.rows = 0
        self.structure = []
    
    def add_row(self, row):
        i = 0
        for v in (x for x in row.split(" ") if len(x) > 0):
            self.structure.append(Point(int(v), self.rows, i))
            i += 1
        self.rows += 1
    
    def mark(self, val):
        for x in self.structure:
            if x.val == val:
                x.is_marked = True
                break
    
    def is_winning(self):
        expected_marked = 5
        for i in range(0, self.rows):
            if len(list(p for p in self.structure if p.x == i and p.is_marked)) == expected_marked:
                return True
            if len(list(p for p in self.structure if p.y == i and p.is_marked)) == expected_marked:
                return True
        return False
    
    def get_unmarked(self):
        return (x for x in self.structure if not x.is_marked)

with open("../input.txt") as f:
    numbers = []
    boards = []
    board = Board()
    for l in f.readlines():
        if not any(c.isdigit() for c in l):
            board = Board()
            boards.append(board)
            continue
        if "," in l:
            numbers = (int(n) for n in l.replace("\n", "").split(","))
        else:
            board.add_row(l.replace("  ", " ").replace("\n", ""))

if __name__ == '__main__':
    finished = False
    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.is_winning():
                finished = True
                unmarked = sum(x.val for x in b.get_unmarked())
                print(n * unmarked)
                break
        if finished:
            break