import os

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint


class Figure:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def perimeter(self):
        return 0.0
    
    def square(self):
        return 0.0
    
    def width(self):
        return 0.0
    
    def height(self):
        return 0.0
    
class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.__x = x
        self.__y = y
        self.w = w
        self.h = h
        
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y   
    
    def perimeter(self):
        return 2*(self.w+self.h)
    
    def square(self):
        return self.w*self.h
    
    def width(self):
        return self.w
    
    def height(self):
        return self.h

# Импортируйте свой файл с фигурами

class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []
        
    def set_figures(self, figures):
        self.__figures = figures
        
    def paintEvent(self, event):
        
        painter = QPainter(self)
        reset_brush = painter.brush()
        
        for figure in self.__figures:
            if not isinstance(figure, Figure):
                continue
            
            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x(), figure.y(), figure.width(), figure.height())
                continue
            
            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.x(), figure.y(), figure.width(), figure.height())
                continue	
                
            if isinstance(figure, CloseFigure): 
                painter.setBrush(QBrush(Qt.blue))
                
                points = []                
                for point in figure:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue
						
	

                                                     
if __name__ == '__main__':

    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()
	
	# Создайте список фигур
    figures = [Rectangle(20, 30, 400, 200), Rectangle(100, 300, 300, 50)]
	
    figure_widget.set_figures(figures)
	
    figure_widget.show()
    sys.exit(app.exec_())
