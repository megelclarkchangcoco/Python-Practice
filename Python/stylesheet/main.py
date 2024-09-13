import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create three QPushButton instances
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        # Create a central widget and set it as the central widget of the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a horizontal box layout
        hbox = QHBoxLayout()

        # Add the buttons to the horizontal box layout
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # Set the layout of the central widget to the horizontal box layout
        central_widget.setLayout(hbox)

        # Set object names for the buttons to apply specific styles
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Apply styles to the buttons using a stylesheet
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }

            QPushButton#button1{
                background-color: red;
            }
             QPushButton#button1:hover{
                background-color: gray;
            }
            QPushButton#button2{
                background-color: green;
            }
             QPushButton#button2:hover{
                background-color: gray;
            }
            QPushButton#button3{
                background-color: blue;
            }
             QPushButton#button3:hover{
                background-color: gray;
            }
        """)


if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Create an instance of MainWindow
    window = MainWindow()
    # Show the main window
    window.show()
    # Execute the application's main loop
    sys.exit(app.exec_())
