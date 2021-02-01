class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def __repr__(self):
        return f"Car of {self.color} color and {self.speed} speed"

dodge = Car("blue", 220)
print(dodge)
# print("{}, {}".format(*vars(dodge).values()))
# print(vars(dodge))
# print(dodge.__dict__)
