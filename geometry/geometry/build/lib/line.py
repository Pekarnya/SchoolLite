from abc import ABC, abstractmethod
import math




class LineSet(ABC):

    @abstractmethod
    def line_length(self, *coordinates):
        ...

class Line2D(LineSet):

    """class representing a 2D line equasion

    |AB|² = (y2 - y1)² + (x2 - x1)²"""


    def line_length(self, *coordinates) -> float:

        """returns the length 2D line (x1, y1, x2, y2)
        inter oy an ox as a list"""


        x1 = coordinates[0]
        y1 = coordinates[1]
        x2 = coordinates[2]
        y2 = coordinates[3]
        length = ((y2 - y1) ** 2) + ((x2 - x1) ** 2)

        return round(math.sqrt(length), 4)



