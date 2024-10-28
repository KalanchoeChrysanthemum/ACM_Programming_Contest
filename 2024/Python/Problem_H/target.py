import math

def main():

    num_shapes = input()

    shapes: list[Shape] = []

    for _ in range(0, int(num_shapes)):
        shape = input().split(' ')
        
        if shape[0] == 'rectangle':
            temp_rect = rectangle(int(shape[1]), int(shape[2]), int(shape[3]), int(shape[4]))
            shapes.append(temp_rect)

        if shape[0] == 'circle':
            temp_circ = circle(int(shape[1]), int(shape[2]), int(shape[3]))
            shapes.append(temp_circ)

    num_shots = int(input())

    shots: list[tuple] = []

    for _ in range(0, num_shots):
        x, y = input().split(' ')

        shot = (int(x), int(y))
        shots.append(shot)

    results = []

    for shot in shots:
        num_hits = 0
        for shape in shapes:
            if shape.is_hitting(shot):
                num_hits += 1

        results.append(num_hits)

    for result in results:
        print(result)

class Shape:
    def is_hitting() -> bool:
        return True

class rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def is_hitting(self, other: tuple) -> bool:
        if other[0] >= self.x1 and other[0] <= self.x2:
            if other[1] >= self.y1 and other[1] <= self.y2:
                return True
            
        return False

class circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center = (center_x, center_y)
        self.radius = radius

    def is_hitting(self, other: tuple) -> bool:
        delta_x = abs(self.center[0] - other[0])
        delta_y = abs(self.center[1] - other[1])

        if delta_x == 0 and delta_y == 0:
            dist_to_radius = 0
        else:
            dist_to_radius = math.sqrt((delta_x ** 2) + (delta_y ** 2))

        if dist_to_radius <= self.radius:
            return True
        
        return False

if __name__ == '__main__':
    main()