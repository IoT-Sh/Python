import math

class Shape:

    def __init__(self):
        self.IV_shape_kind = " "
        self.IV_shape_color = " "

    @property
    def PIV_shape_kind(self):
        return self.IV_shape_kind

    @property
    def PIV_shape_color(self):
        return self.IV_shape_color

    #set shape kind
    def setShapeKind(self, shape_kind):

        debug_data = []
        return_msg = "Shape:setShapeKind: "

        if type(shape_kind) == str and shape_kind in ["Circle","Square","Rectangle"]:
            self.IV_shape_kind = shape_kind

        else:
            return_msg += f"{shape_kind} is invalid Shape. Shape type must be Circle, Square or Rectangle"
            return {"success": False, "return_msg": return_msg, "debug_data": debug_data}

        return {"success": True, "return_msg": return_msg, "debug_data": debug_data}

    #set shape color
    def setShapeColor(self, shape_color):

        debug_data = []
        return_msg = "Shape:setShapeColor: "

        if type(shape_color) == str and shape_color in ["Red","Blue","Green","Violate","Yellow","White"]:
            self.IV_shape_color = shape_color

        else:
            return_msg += f"{shape_color} is invalid Color. Color should be Red, Blue, Green, Violate, Yellow, White"
            return {"success": False, "return_msg": return_msg, "debug_data": debug_data}

        return {"success": True, "return_msg": return_msg, "debug_data": debug_data}

class Circle(Shape):

    def __init__(self):
        self.IV_circle_radius = 0.0


    @property
    def PIV_circle_radius(self):
        return self.IV_circle_radius

    #function to set circle radius
    def setCircleRadius(self, circle_radius):

        debug_data = []
        return_msg = "Circle:setCircleRadius "

        #input validation
        if type(circle_radius) != str and circle_radius > 0.0:
            self.IV_circle_radius = circle_radius

        else:
            return_msg += f"value should be greater than 0. value {circle_radius} is an invalid radius"
            return { "success": False, "return_msg": return_msg, "debug_data": debug_data }

        return { "success": True, "return_msg": return_msg, "debug_data": debug_data}

    def calculateArea(self):

        debug_data = []
        return_msg = "Circle:calculateArea"

        area = math.pi*self.IV_circle_radius*self.IV_circle_radius

        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "area": area}


#Class for Square Shape
class Square(Shape):
    def __init__(self):
        self.IV_square_side = 0.0

    @property
    def PIV_square_side(self):
        return self.IV_square_side

    #function to set Square side
    def setSquareSide(self, square_side):

        debug_data = []
        return_msg = "Square:setSquareSide "

        if type(square_side) != str and square_side > 0.0:
            self.IV_square_side = square_side

        else:
            return_msg += f"value should be greater than 0. value {square_side} is an invalid radius"
            return { "success": False, "return_msg": return_msg, "debug_data": debug_data }

        return {"success": True, "return_msg": return_msg, "debug_data": debug_data}

    def calculateArea(self):
        return_msg = "Square:calculateArea"
        debug_data = []
        area = self.IV_square_side*self.IV_square_side
        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "area": area}


#Class for Rectangle Shape
class Rectangle(Shape):

    def __init__(self):

        self.IV_rectangle_dimension = {}
        self.IV_rectangle_dimension["Length"] = 0.0
        self.IV_rectangle_dimension["Width"] = 0.0

    @property
    def PIV_rectangle_dimension(self):
        return self.IV_rectangle_dimension

    #function to set Rectangle side
    def setRectangleDimension(self, Length, Width):

        debug_data = []
        return_msg = "Square:setRectangleDimension "

        if type(Length) != str and Length > 0.0:
            self.IV_rectangle_dimension["Length"] = Length

        if type(Width) != str and Width > 0.0:
            self.IV_rectangle_dimension["Width"] = Width

        else:
            return_msg += f"value should be greater than 0. value {rectangle_dimension} is an invalid radius"
            return { "success": False, "return_msg": return_msg, "debug_data": debug_data }

        return {"success": True, "return_msg": return_msg, "debug_data": debug_data}

    #Calculate Rectangle Area
    def calculateArea(self):
        return_msg = "Rectangle:calculateArea"
        debug_data = []
        area = self.IV_rectangle_dimension["Length"]*self.IV_rectangle_dimension["Width"]
        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "area": area}


#test function
def testShape():

    shape_property = Shape()

    #valid kind
    shape_kind = "Circle"
    shape_property.setShapeKind(shape_kind)
    kind = shape_property.PIV_shape_kind
    print(kind)

    #invalid kind
    shape_color = 2
    shape_property.setShapeColor(shape_color)
    kind = shape_property.PIV_shape_kind
    print(kind)

    #valid color
    shape_color = "Red"
    shape_property.setShapeColor(shape_color)
    color = shape_property.PIV_shape_color
    print(color)

    #invalid color
    shape_color = 5
    shape_property.setShapeColor(shape_color)
    color = shape_property.PIV_shape_color
    print(color)


    #test class Circle
    circle_property = Circle()
    circle_radius = 5.2
    circle_property.setCircleRadius(circle_radius)

    get_radius = circle_property.PIV_circle_radius
    print(get_radius)

    circle_Area = circle_property.calculateArea()
    print(circle_Area)

    #test class Square
    square_property = Square()
    square_side = 13.1
    square_property.setSquareSide(square_side)


    get_side = square_property.PIV_square_side
    print(get_side)

    square_Area = square_property.calculateArea()
    print(square_Area)

    #test class Rectangle
    rectangle_property = Rectangle()
    rectangle_length = 5.2
    rectangle_width = 3.9
    rectangle_property.setRectangleDimension(rectangle_length, rectangle_width)

    get_dimension = rectangle_property.PIV_rectangle_dimension
    print(get_dimension)

    rectangle_Area = rectangle_property.calculateArea()
    print(rectangle_Area)

testShape()
