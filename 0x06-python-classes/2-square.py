#!/usr/bin/python3
"""Square class """


class Square:
    """ Square class  defines a square by size"""
    def __init__(self, size=0):
        """ The __init__ method  used to initialize the object """
        self.__size = size
        if type(size) != "int":
            print("size must be an integer")
            if type(size) == "int" and size < 0:
                print("size must be >= 0")
