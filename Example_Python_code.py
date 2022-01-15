import math

class Shape:

    def __init__(self, IV_shape_kind, IV_shape_color):
        self.IV_shape_kind = " "
        self.IV_shape_color = " "

    @property
    def kinds(self):
        return self.IV_shape_kind

    @property
    def color(self):
        return self.IV_shape_color

    def setShapeKind(self, shape_kind):

        debug_data = []
        return_msg = "Shape:setShapeKind: "

        if shape_kind and shape_kind in ["Circle","Square","Rectangle"]:
            self.IV_shape_kind = shape_kind

        else:
            return_msg += "invalid Shape"
            return {'success': False, 'return_msg': return_msg,'debug_data': debug_data}

        return {'success': True, 'return_msg': return_msg,'debug_data': debug_data}

    def setShapeColor(self, shape_color):

        debug_data = []
        return_msg = "Shape:setShapeColor: "

        if shape_color and shape_color in ["Red","Blue","Green","Violate","Yellow","White"]:
            self.IV_shape_color = shape_color

        else:
            return_msg += "invalid Color"
            return {'success': False, 'return_msg': return_msg,'debug_data': debug_data}

        return {'success': True, 'return_msg': return_msg,'debug_data': debug_data}


class Circle(Shape):

    def __init__(self, IV_circle_radius):
        self.IV_circle_radius = 0.0


    @property
    def circle_radius(self):
        return self.radius

    #function to set circle radius
    def setCircleRadius(self, circle_radius):

        debug_data = []
        return_msg = "Circle:setCircleRadius "

        #input validation
        if type(circle_radius) != str and circle_radius > 0.0:
            self.IV_circle_radius = circle_radius

        else:
            return_msg += "value should be greater than 0. value {} ia in invalid radius".format(circle_radius)
            return { "success": False, "return_msg": return_msg, "debug_data": debug_data }

        return { "success": True, "return_msg": return_msg, "debug_data": debug_data, "radius": self.IV_radius}

    def calculateArea(self):

        debug_data = []
        return_msg = "Circle:calculateArea"

        area = 2*math.pi*self.circle_radius
        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "area": area}


#Class for Square Shape
class Square(Shape):
    def __init__(self, IV_square_side):
        self.IV_square_side = None


    #function to set Square side
    def setSquareSide(self, square_side):

        debug_data = []
        return_msg = "Square:setSquareSide "

        if type(square_side) != str and square_side > 0.0:
            self.IV_square_side = square_side

        else:
            return_msg += "value should be greater than 0. value {} ia in invalid radius".format(circle_radius)
            return { "success": False, "return_msg": return_msg, "debug_data": debug_data }

        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "square_side": self.IV_square_side}

    def calculateArea(self):
        return_msg = "Square:calculateArea"
        debug_data = []
        area = self.IV_square_side*self.IV_square_side
        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "area": area}


#Class for Rectangle Shape
class Rectangle(Shape):
    def __init__(self, IV_rectangle_dimension):
        self.IV_rectangle_dimension["Length"] = None
        self.IV_rectangle_dimension["Width"] = None


    #function to set Rectangle side
    def setSquareSide(self, Length, Width):

        debug_data = []
        return_msg = "Square:setRectangleDimension "

        if type(Length) != str and Length > 0.0:
            self.IV_rectangle_dimension["Length"] = Length

        if type(Width) != str and Width > 0.0:
            self.IV_rectangle_dimension["Width"] = Width

        else:
            return_msg += "value should be greater than 0. value {} ia in invalid radius".format(circle_radius)
            return { "success": False, "return_msg": return_msg, "debug_data": debug_data }

        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "rectangle_dimension": self.IV_rectangle_dimension}

    #Calculate Rectangle Area
    def calculateArea(self):
        return_msg = "Rectangle:calculateArea"
        debug_data = []
        area = self.IV_rectangle_dimension["Length"]*self.IV_rectangle_dimension["Width"]
        return {"success": True, "return_msg": return_msg, "debug_data": debug_data, "area": area}
