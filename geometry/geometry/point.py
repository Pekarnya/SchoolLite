from abc import ABC, abstractmethod


class Point2D():

    """class for describing Point2D objects"""

    def point2D( **points: dict) -> tuple:

        """returns a tuple of 2D coordinates"""
        
        coordinates = points.get("point1") + points.get("point2")

        match points:

            case {"point3": list}:

                coordinates += points.get("point3")

        match points:

            case {"point4": list}:

                coordinates += points.get("point4")


        return coordinates



        
