import os

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint
# from painter import FigureWidget

from abc import abstractmethod

class Figure:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @abstractmethod
    def perimeter(self):
        ...

    @abstractmethod
    def square(self):
        ...

    @property
    def width(self):
        return 0

    @property
    def height(self):
        return 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError
        self._y = y

class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        # self.__x = x
        # self.__y = y
        super().__init__(x, y)
        self.width = w
        self.height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        # if isinstance(height, int):
        #     raise TypeError
        self._height = height


    # def perimeter(self):
    #     return 2*(self.w+self.h)
    #
    # def square(self):
    #     return self.w*self.h
    #
    # def width(self):
    #     return self.w
    #
    # def height(self):
    #     return self.h

# Импортируйте свой файл с фигурами

class Ellipse(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        # self.__x = x
        # self.__y = y
        super().__init__(x, y)
        self.width = w
        self.height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        # if isinstance(height, int):
        #     raise TypeError
        self._height = height

# class CloseFigure(Figure):
#     def __init__(self, x=0, y=0, w=0, h=0):
#         # self.__x = x
#         # self.__y = y
#         super().__init__(x, y)
#         self.width = w
#         self.height = h
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, width):
#         self._width = width
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, height):
#         # if isinstance(height, int):
#         #     raise TypeError
#         self._height = height

class CloseFigure(Figure):
    def __init__(self, *args):
        self.d = [{'x': x0, 'y': y0},
                  {'x': x1, 'y': y1}]






