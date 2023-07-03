#!/usr/bin/python3
"""Rectangle class """


class Rectangle:
    """ Rectangle class is an empty class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ initialize Rectangle objects, """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the value of __width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of __width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets the value of __height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of __height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value