__author__ = 'CheD'

from math import hypot

__all__ = (
    'Point',
)


class Point:
    """
    A class for Point(x,y) representing.
    Supported types: integer, floating.

    Usage:
    >>> point = Point()
    >>> point
    Point: (x = 0, y = 0)
    >>> point1 = Point(10, 20)
    >>> point1
    Point: (x = 10, y = 20)
    >>> point2 = point1
    >>> point1 == point2
    True
    >>> point == point1
    False
    >>> point.distance(point1)
    22.36
    """

    def __init__(self, x=0, y=0):
        """
        The initializer.

        :param x: x-coordinate. Possible values: integer, float.
        :param y: y-coordinate. Possible values: integer, float.
        """

        self._x = x
        self._y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f'({self.x}, {self.y})'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, other):
        self._x = other

    @y.setter
    def y(self, other):
        self._y = other

    def distance(self, other):
        """
        The method counts distance between two points.

        :param other: type of arg is Point
        :return: float in the form ("%.2f")
        """
        return round(hypot(self.x - other.x, self.y - other.y), 2)
