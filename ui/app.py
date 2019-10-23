import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request   
class app():
    def __init__(self):
        app = QApplication(sys.argv)
        w = Window()
        app.exec_()

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,400,400)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        
        self.labcanvas = QLabel()
        self.canvas = QPixmap(400, 400)
        self.canvas.fill(QColor(255, 255, 255))
        self.labcanvas.setPixmap(self.canvas)

        self.pen_color = QColor(0, 0, 0)
        self.setMouseTracking(True)
        self.labcanvas.setMouseTracking(True)
#        self.canvas.setMouseTracking(True)
#        self.setInteractive(True)
        self.layout.addWidget(self.labcanvas)
        
        self.show()
        
    

    def mouseMoveEvent(self, e):
        print("REACHED :"+str(e.x())+ " | "+str(e.y()))
        painter = QPainter(self.labcanvas.pixmap())
        
        p = painter.pen()
        p.setWidth(5)
        p.setColor(self.pen_color)
        painter.setPen(p)
        
        painter.drawPoint(e.x(), e.y())

        self.update()

    def take_screenshot(self):
        filename = "test"
        print("Screenshot")
        self.canvas.save(filename, 'jpg')
       
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.take_screenshot()
            self.close()

