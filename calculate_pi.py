from math import sqrt
import sys
from random import uniform

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        distance = sqrt(dx * dx + dy * dy)
        return distance

class CalculatorPi:
    def __init__(self, sum_points: int):
        self.radius = 10
        self.center = Point(0, 0)
        self.sum_points = sum_points
        self.points_list = []
        pass

    def get_one_random(self) -> float:
        return uniform(-self.radius, self.radius)

    def put_points(self, sum_points):
        for _ in range(self.sum_points):
            one_x = self.get_one_random()
            one_y = self.get_one_random()
            one_point = Point(one_x, one_y)
            self.points_list.append(one_point)
            
    def sum_points_in_circle(self) -> int:
        sum = 0
        for one_point in self.points_list:
            distance_to_center = one_point.distance_to(self.center)
            if distance_to_center <= self.radius:
                sum += 1
        return sum

    def get_pi(self) -> float:
        self.put_points(self.sum_points)
        sum_points_in_circle = self.sum_points_in_circle()
        pi = (sum_points_in_circle / self.sum_points) * 4
        return pi
    
if __name__ == '__main__':
    for i in range(1, 7):
        n = 1 * 10 ** i
        caculator = CalculatorPi(n)
        pi = caculator.get_pi()
        print(f'point number {n}, pi {pi}')
    pass
