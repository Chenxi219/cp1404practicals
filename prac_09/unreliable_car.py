from prac_09.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_int = random.randint(1, 100)
        if random_int < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven