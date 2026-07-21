# from abc import ABC,abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):

#     def __init__(self,r) :
#         self.r=r

#     def calculate_area(self):
#         return 3.1416 * self.r * self.r

#     def calculate_perimeter(self):
#         return 2 * 3.1416 * self.r

# class Square(Shape):
#     def __init__(self,side):
#         self.side=side

#     def calculate_area(self):
#         return self.side * self.side

#     def calculate_perimeter(self):
#         return 4 * self.side

# class Rectangle(Shape):
#     def __init__(self,height,weight):
#         self.weight=weight
#         self.height=height

#     def calculate_area(self):
#         return self.height * self.weight

#     def calculate_perimeter(self):
#         return 2 * (self.height + self.weight)

# class ShapeFactory:
#     def create_shape(self,shape_name):
#         if shape_name == "circle":
#             userinput = float(input("Enter radius: "))
#             return Circle(userinput)

#         elif shape_name == "square":
#             userinput = float(input("Enter side: "))
#             return Square(userinput)

#         elif shape_name == "rectangle":
#             userinput1 = float(input("Enter height: "))
#             userinput2 = float(input("Enter width: "))
#             return Rectangle(userinput1,userinput2)

# def shape_client():
#     shapefactory = ShapeFactory()
#     shape_name = input("Enter your shape name: ")
#     shape = shapefactory.create_shape(shape_name)

#     print(f"Type of shape has {shape_name}")
#     print(shape.calculate_area())
#     print(shape.calculate_perimeter())


# shape_client()


# from abc import ABC,abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def draw(self):
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("Circle drawing")

# class Rectangle(Shape):
#     def draw(self):
#         print("Rectangle drawing")

# class Square(Shape):
#     def draw(self):
#         print("Square drawing")

# class ShapeFactory:
#     def getShape(self,name):
#         if name == "circle":
#             return Circle()

#         elif name == "square":
#             return Square()

#         elif name == "rectangle":
#             return Rectangle()

# def Shape_client():
#     shape_factory = ShapeFactory()
#     while True:
#         shape_name = input("Enter your shape name: ")
#         shape = shape_factory.getShape(shape_name)
#         shape.draw()
#         if shape_name == "quit":
#             break

# Shape_client()


# from abc import ABC,abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.1416 * self.radius * self.radius

#     def calculate_perimeter(self):
#         return 2 * 3.1416 * self.radius

# class Square(Shape):

#     def __init__(self,side):
#         self.side = side

#     def calculate_area(self):
#         return self.side * self.side

#     def calculate_perimeter(self):
#         return 4 * self.side

# class Rectangle(Shape):

#     def __init__(self,height,width):
#         self.height = height
#         self.width = width

#     def calculate_area(self):
#         return self.height * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.height + self.width)

# class ShapeFactory:
#     def create_shape(self,shape_name):
#         if shape_name == "circle":
#             user_input = float(input("Enter radius: "))
#             return Circle(user_input)

#         elif shape_name == "square":
#             user_input = float(input("Enter side: "))
#             return Square(user_input)

#         elif shape_name == "rectangle":
#             user_input1 = float(input("Enter height: "))
#             user_input2 = float(input("Enter width: "))
#             return Rectangle(user_input1,user_input2)


# def shape_client():
#     shape_factory = ShapeFactory()
#     while True:
#         shape_name = input("Enter shape name: ")
#         shape = shape_factory.create_shape(shape_name)
#         print(f"The shape has: {shape_name}\nArea = {shape.calculate_area()}\nPerimeter = {shape.calculate_perimeter()}")

#         if shape_name == "quit":
#             break
# shape_client()


# from abc import ABC, abstractmethod


# class FlatShape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class SolidShape(ABC):

#     @abstractmethod
#     def volume(self):
#         pass

#     @abstractmethod
#     def surface_area(self):
#         pass


# class Circle2D(FlatShape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.1416 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.1416 * self.radius


# class Square2D(FlatShape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

#     def perimeter(self):
#         return 4 * self.side


# class Sphere3D(SolidShape):
#     def __init__(self, radius):
#         self.radius = radius

#     def volume(self):
#         return (4 / 3) * 3.1416 * self.radius**3

#     def surface_area(self):
#         return 4 * 3.1416 * self.radius**2


# class Cube3D(SolidShape):
#     def __init__(self, side):
#         self.side = side

#     def volume(self):
#         return self.side**3

#     def surface_area(self):
#         return 6 * self.side**2


# class ShapeFactory(ABC):

#     @abstractmethod
#     def create_flat_shape(self):
#         pass

#     @abstractmethod
#     def create_solid_shape(self):
#         pass


# class CircleSphereFactory(ShapeFactory):
#     def create_flat_shape(self):
#         r = float(input("Enter radius: "))
#         return Circle2D(r)

#     def create_solid_shape(self):
#         s = float(input("Enter radius: "))
#         return Sphere3D(s)


# class SquareCubeFactory(ShapeFactory):
#     def create_flat_shape(self):
#         r = float(input("Enter side: "))
#         return Square2D(r)

#     def create_solid_shape(self):
#         s = float(input("Enter side: "))
#         return Cube3D(s)


# class FactoryProducer:
#     def get_factory(self, choice):
#         if choice == "circle":
#             return CircleSphereFactory()
#         elif choice == "square":
#             return SquareCubeFactory()


# def client():
#     choice = input("Enter shape name: ")
#     dimension = input("Enter dimension name: ")
#     factory = FactoryProducer().get_factory(choice)

#     if dimension == "flat":
#         shape = factory.create_flat_shape()
#         print(f"Area = {shape.area()}")
#         print(f"Perimeter = {shape.perimeter()}")

#     elif dimension == "solid":
#         shape = factory.create_solid_shape()
#         print(f"Volume = {shape.volume()}")
#         print(f"Surface are = {shape.surface_area()}")


# client()


# from abc import ABC,abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def draw(self):
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("Drawing circle")

# class Square(Shape):
#     def draw(self):
#         print("Drawing square")

# class Rectangle(Shape):
#     def draw(self):
#         print("Drawing rectangle")

# class ShapeFactory:
#     def get_factory(self,Shape):
#         if Shape == "circle":
#             return Circle()

#         elif Shape == "square":
#             return Square()

#         elif Shape == "rectangle":
#             return Rectangle()

# def shape_client():
#     shape_name = input("Enter a shape name: ")
#     factory = ShapeFactory().get_factory(shape_name)
#     factory.draw()

# shape_client()


# from abc import ABC,abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.1416 * self.radius * self.radius

#     def calculate_perimeter(self):
#         return 2 * 3.1416 * self.radius

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side

#     def calculate_area(self):
#         return self.side * self.side

#     def calculate_perimeter(self):
#         return 4 * self.side

# class Rectangle(Shape):
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width

#     def calculate_area(self):
#         return self.height * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.height + self.width)


# class ShapeFactory:
#     def create_shape(self,shape_name):
#         if shape_name == "circle":
#             radius = float(input("Enter radius: "))
#             return Circle(radius)

#         elif shape_name == "square":
#             side = float(input("Enter side: "))
#             return Square(side)

#         elif shape_name == "rectangle":
#             height = float(input("Enter height: "))
#             width = float(input("Enter width: "))
#             return Rectangle(height,width)

# def shape_client():
#     while True:
#         shape_name = input("Enter shape name: ")
#         factory = ShapeFactory().create_shape(shape_name)
#         print(f"Shape: {shape_name}\nArea = {factory.calculate_area()}")
#         print(f"Perimeter = {factory.calculate_perimeter()}")

#         if shape_name == "quit":
#             break

# shape_client()


from abc import ABC, abstractmethod


class FlatShape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class SolidShape(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass


class Circle2D(FlatShape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r

    def perimeter(self):
        return 2 * 3.1416 * self.r


class Square2D(FlatShape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s

    def perimeter(self):
        return 4 * self.s


class Sphere3D(SolidShape):
    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4 / 3) * 3.1416 * self.r**3

    def surface_area(self):
        return 4 * 3.1416 * self.r**2


class Cube3D(SolidShape):
    def __init__(self, s):
        self.s = s

    def volume(self):
        return self.s**3

    def surface_area(self):
        return 6 * self.s**2


class ShapeFactory(ABC):

    @abstractmethod
    def create_flat_shape(self):
        pass

    @abstractmethod
    def create_solid_shape(self):
        pass


class CircleSphereFactory(ShapeFactory):
    def create_flat_shape(self):
        r = float(input("Enter radius: "))
        return Circle2D(r)

    def create_solid_shape(self):
        s = float(input("Enter radius: "))
        return Sphere3D(s)


class SquareCubeFactory(ShapeFactory):
    def create_flat_shape(self):
        r = float(input("Enter side: "))
        return Square2D(r)

    def create_solid_shape(self):
        s = float(input("Enter cube side: "))
        return Cube3D(s)


class FactoryProducer:
    def get_factory(self, choice):
        if choice == "circle":
            return CircleSphereFactory()
        elif choice == "square":
            return SquareCubeFactory()


def client():
    factory_name = input("Enter factory name: ")
    dimension = input("Enter dimension name: ")
    factory = FactoryProducer().get_factory(factory_name)

    if dimension == "flat":
        shape = factory.create_flat_shape()
        print(f"Area = {shape.area()}")
        print(f"Perimeter = {shape.perimeter()}")

    elif dimension == "solid":
        shape = factory.create_solid_shape()
        print(f"Volume = {shape.volume()}")
        print(f"Surface area = {shape.surface_area}")
client()