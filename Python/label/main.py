import sys  # Import the sys module for system-specific parameters and functions
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel  # Import necessary PyQt5 widgets
from PyQt5.QtGui import QFont, QIcon  # Import QFont and QIcon from PyQt5 for font and icon handling
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):  # Define a class MainWindow that inherits from QMainWindow
    def __init__(self):  # Initialize the MainWindow class
        super().__init__()  # Call the parent class (QMainWindow) constructor
        self.setWindowTitle("My cool first GUI")  # Set the window title
        self.setGeometry(700, 300, 500, 500)  # Set the window size and position (x, y, width, height)
        self.setWindowIcon(QIcon("mylove.jpg"))  # Set the window icon
        label = QLabel("Hi Liza", self)  # Create a QLabel widget with text "Hi Liza" and set it as a child of MainWindow
        label.setFont(QFont("Arial", 40))  # Set the font of the label to Arial with size 40
        label.setGeometry(0,0,500,100) # expand label size
        label.setStyleSheet("color: Red;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # set color of label
        label.setAlignment(Qt.AlignCenter) # Align in Verticaly Center


def main():  # Define the main function
    app = QApplication(sys.argv)  # Create an instance of QApplication
    window = MainWindow()  # Create an instance of MainWindow
    window.show()  # Show the MainWindow
    sys.exit(app.exec_())  # Execute the application and exit when the window is closed

if __name__ == "__main__":  # Check if the script is being run directly (not imported)
    main()  # Call the main function
