from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

# class Square(Shape):
#     def __init__(self,size):
#         self.size=size

#     def calculate_area(self):
#         return self.size * self.size

#     def calculate_perimeter(self):
#         return 4 * self.size

# square=Square(5)
# print(square.calculate_area())
# print(square.calculate_perimeter())


# class Vehicle(ABC):
#     def __init__(self,name):
#         self.name=name

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         return f"{self.name} started"

#     def stop(self):
#         return f"{self.name} stopped"

# car = Car("Audi")
# print(car.start())
# print(car.stop())


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Draw Circle")


class Square(Shape):
    def draw(self):
        print("Draw square")


class Rectangle(Shape):
    def draw(self):
        print("Draw rectangle")


class ShapeFactory:
    def getShape(self, name):
        if name == "Circle":
            return Circle()
        elif name == "Square":
            return Square()
        elif name == "Rectangle":
            return Rectangle()


def shape_client():
    shape_factory = ShapeFactory()
    shape_name = input("Enter shape name: ")
    shape = shape_factory.getShape(shape_name)
    shape.draw()


shape_client()
