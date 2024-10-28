class ex:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def is_near(self, other) -> bool:
        if abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1:
            return True
        return False
    
    def on_edge(self) -> bool:
        if self.x == 0 or self.x == 6:
            return True
        if (self.y == 0 and self.x == 0) or (self.y == 6 and self.x == 6):
            return True
        return False

def main():
    num_cases = int(input())

    for _ in range(0, num_cases):
        
        board: list[str] = []

        # str -> list[char]

        for _ in range(0, 7):
            board.append(input())

        exes = []
        id = 1


        for y, row in enumerate(board):
            for x, char in enumerate(row):
                if char == 'X':
                    exes.append(ex(x, y), id)
                    id += 1


def solve(exes: list[ex], prev_moves: list, depth: int, moved_ex: ex) -> int:

    if check_3_by_3(exes):
        return depth
    
    any_on_edge = False

    for ex in exes:
        if ex.on_edge():
            any_on_edge = True
            break

    if not any_on_edge:
        return depth
    
    if prev_moves.contains((moved_ex[0], moved_ex[1])):
        return depth
        
def check_3_by_3(exes: list[ex]) -> bool:
    for first_ex in exes:
        count = 0
        for second_ex in exes:
            if first_ex.id == second_ex.id:
                continue
            if first_ex.is_near(second_ex):
                count += 1

        if count == 8:
            return True
    return False


if __name__ == '__main__':
    main()