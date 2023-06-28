#!/usr/bin/python3
"""Square class """


class Square:
    """ class square defines a square by size """
    def __init__(self, size=0):
        """ initialize square objects, """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ gets the value of __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of __size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2
