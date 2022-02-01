class Car:
    def __init__(self,color,miles):
        self.color = color
        self.miles = miles

    def __str__(self):
        return "The %s car has %d miles." %(self.color, self.miles)

car1 = Car("blue", 20000)
car2 = Car("red", 30000)

my = {"a":car1, "b":car2}
print(my["a"].color)
print(car1)
print(car2)
