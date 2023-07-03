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

    def area(self):
        """ returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """  print the rectangle with the character # """
        char = ""
        if self.__width == 0 or self.__height == 0:
            return char
        for i in range(self.__height):
            for j in range(self.__width):
                char += "#"
            char += '\n'
        return char[:-1]

    def __repr__(self):
        """  return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)
