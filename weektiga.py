import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Week 3 - (F1D022127 - Kayla Mizanti )")
        self.setGeometry(100, 100, 600, 400)
        
        self.label = QLabel("Start!", self)
        self.label.setGeometry(250, 180, 120, 30)
        self.label.setStyleSheet("background-color: pink; border: 1px solid black;")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
    
    def mouseMoveEvent(self, event):
        self.label.setText(f"X: {event.x()}, Y: {event.y()}")
    
    def enterEvent(self, event):
        self.reposition_label()
    
    def reposition_label(self):
        max_x = self.width() - self.label.width()
        max_y = self.height() - self.label.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.label.move(new_x, new_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())