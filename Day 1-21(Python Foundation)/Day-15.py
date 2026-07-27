# # class Animal:
# #     def __init__(self,name,sound):
# #         self.name = name
# #         self.sound = sound

# #     def speak(self):
# #         print(f"{self.name} says {self.sound}")

# #     def eat(self,food):
# #         print(f"{self.name} is eating {food}")

# # class Dog(Animal):
# #     def fetch(self):
# #         print(f"{self.name} fetches the ball")

# # class Cat(Animal):
# #     def purr(self):
# #         print(f"{self.name} purrssssss")


# # dog = Dog("Dog","Gheu")
# # dog.speak()
# # dog.fetch()


# # class Animal:
# #     def __init__(self, name):
# #         print(f"Animal __init__ চলছে — name={name}")
# #         self.name = name


# # class Dog(Animal):
# #     def __init__(self, name, breed):
# #         print("Dog __init__ শুরু")
# #         super().__init__(name)
# #         print("Animal __init__ শেষ, Dog-এ ফিরলাম")
# #         self.breed = breed
# #         print("Dog __init__ শেষ")


# # dog = Dog("Bruno", "Labrador")


# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def area(self):
#         return 0

#     def describe(self):
#         print(f"I am a {self.color} shape with area {self.area()}")


# class Circle(Shape):
#     def __init__(self, color,radius):
#         super().__init__(color)
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self, color,width,height):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height

# c = Circle("red", radius=5)
# r = Rectangle("blue", width=4, height=6)

# c.describe()
# r.describe()


# class Employee:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary

#     def get_salary(self):
#         return self.base_salary

#     def introduce(self):
#         print(f"I am {self.name}, salary: {self.get_salary()}")

# class Manager(Employee):
#     def __init__(self, name, base_salary,bonus):
#         super().__init__(name, base_salary)
#         self.bonus = bonus
#     def get_salary(self):
#         return self.base_salary + self.bonus

# class Intern(Employee):
#     def __init__(self, name, base_salary,stipend_percentage):
#         super().__init__(name, base_salary)
#         self.stipend_percentage = stipend_percentage

#     def get_salary(self):
#         return self.base_salary * self.stipend_percentage


# m = Manager("Rahim", 50000, bonus=10000)
# i = Intern("Karim", 50000, stipend_percentage=0.2)

# m.introduce()  # I am Rahim, salary: 60000
# i.introduce()  # I am Karim, salary: 10000.0


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")

    def info(self):
        print(f"Brand: {self.brand}")
        self.move()


class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def move(self):
        super().move()
        print("Vroom Vroom")


class Boat(Vehicle):
    def __init__(self, brand, speed, water_type):
        super().__init__(brand, speed)
        self.water_type = water_type

    def move(self):
        super().move()
        print(f"Sailing on the {self.water_type}")


c = Car("Toyota", 120, num_doors=4)
b = Boat("Yamaha", 60, water_type="sea")
d = Car("Ferrari", 250, num_doors=5)

c.info()
b.info()
d.info()
