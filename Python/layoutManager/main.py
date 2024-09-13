import sys  # Import the sys module for system-specific parameters and functions
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)  # Import necessary PyQt5 widgets and layouts

class MainWindow(QMainWindow):  # Define a class MainWindow that inherits from QMainWindow
    def __init__(self):  # Initialize the MainWindow class
        super().__init__()  # Call the parent class (QMainWindow) constructor
        self.setWindowTitle("Layouts")  # Set the window title
        self.setGeometry(700, 300, 500, 500)  # Set the window size and position (x, y, width, height)
        self.initUI()  # Call the initUI method to set up the user interface

    def initUI(self):  # Define the initUI method to set up the user interface
        central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget for the main window

        # Create QLabel widgets with text "1", "2", "3", "4", "5" and set them as children of MainWindow
        label1 = QLabel("1", self)
        label2 = QLabel("2", self)
        label3 = QLabel("3", self)
        label4 = QLabel("4", self)
        label5 = QLabel("5", self)

        # Set background colors for the labels using CSS styles
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        vbox = QGridLayout()  # Create a QGridLayout instance

        # Add the labels to the grid layout at specified positions (row, column)
        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 0, 1)
        vbox.addWidget(label3, 1, 0)
        vbox.addWidget(label4, 1, 1)
        vbox.addWidget(label5, 1, 2)

        central_widget.setLayout(vbox)  # Set the layout for the central widget

def main():  # Define the main function
    app = QApplication(sys.argv)  # Create an instance of QApplication
    window = MainWindow()  # Create an instance of MainWindow
    window.show()  # Show the MainWindow
    sys.exit(app.exec_())  # Execute the application and exit when the window is closed

if __name__ == "__main__":  # Check if the script is being run directly (not imported)
    main()  # Call the main function
