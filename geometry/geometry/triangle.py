
from point import Point2D
from line import Line2D
import math

class Triangle():


    def __height(**params):

        """Don`t call this function directly"""

        perimetr = Triangle.__perimetr(**params)
        len_lineA = params["len_lineA"]
        len_lineB = params["len_lineB"]
        len_lineC = params["len_lineC"]
        half_perimetr = 0.5 * perimetr


        numerator = 2 *(math.sqrt((half_perimetr * (half_perimetr - len_lineA)*(half_perimetr - 
        len_lineB)*(half_perimetr - len_lineC))))
        height = numerator / len_lineA

        return height


    def __perimetr(**params: dict) -> float:

        """Don`t call this function directly"""

        perimetr = (params["len_lineA"] + params["len_lineB"] + params["len_lineC"])
        perimetr = round(perimetr, 4)

        return perimetr

    def __area(**points):
        
        params = Triangle.__get_params(**points)
        height = Triangle.__height(**params)
        len_lineA = params["len_lineA"]
        area = (len_lineA * height) / 2
        round_area = round(area, 4)
        

        return round_area




    def __get_params(**points) -> dict:

        """private method to get the parameters of a triangle"""

        coordinates = Point2D.point2D(**points) 

        lineA = tuple((None, coordinates[0], coordinates[1], coordinates[2],
        coordinates[3]))

        lineB = tuple((None, coordinates[0], coordinates[1], coordinates[4], 
        coordinates[5]))

        lineC = tuple((None, coordinates[2], coordinates[3], coordinates[4],
        coordinates[5]))

        len_lineA = Line2D.line_length(*lineA)
        len_lineB = Line2D.line_length(*lineB)
        len_lineC = Line2D.line_length(*lineC)

        params = dict()
        params["lineA"] = lineA
        params["lineB"] = lineB
        params["lineC"] = lineC
        params["coordinates"] = coordinates
        params["len_lineA"] = len_lineA
        params["len_lineB"] = len_lineB
        params["len_lineC"] = len_lineC

        return params



    def perimetr(**points):

        """calculates the perimeter of the triangle

        Enter 3 points (point1 = (x, y) etc

        Returns:
            float: length of perimeter
        """

        params = Triangle.__get_params(**points)
        perimetr = Triangle.__perimetr(**params)

        return perimetr


    def sqare (**points):

        """A square is inscribed in a triangle
        Takes 3 points of triangle (Point1 = (x, y) etc

        """
        params = Triangle.__get_params(**points)
        height = Triangle.__height(**params)
        side_of_square = (params["len_lineA"] * height) / (height + params["len_lineA"])

        return side_of_square

    def area( **points):

        """calculates the area of the triangle"""

        area = Triangle.__area(**points)

        return area

    def height( **points):

        params = Triangle.__get_params(**points)
        height = Triangle.__height(**params)

        return height

