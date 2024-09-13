import sys
from tkinter import Label

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Image")
        self.setGeometry(700,300,500,500)

        label1 = QLabel("My Loves",self)
        label1.setGeometry(0,0,500,100)
        label1.setFont(QFont("Arial", 40))
        label1.setStyleSheet("background-color: #6fdcf7;")
        label1.setAlignment(Qt.AlignCenter) # Align in Verticaly Center


        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("mylove.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                        label.width(),
                        label.height()) # Align in Verticaly Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()