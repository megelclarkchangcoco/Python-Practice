import sys

from PyQt5.QtCore import QLine  # Import QLine from PyQt5.QtCore (Note: This import is not used and can be removed)
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

# Define the main window class inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the parent class (QMainWindow) constructor
        self.setGeometry(700, 300, 500, 500)  # Set the window size and position
        self.line_edit = QLineEdit(self)  # Create a line edit widget
        self.button = QPushButton("Submit", self)  # Create a button widget
        self.initUI()  # Initialize the UI components

    def initUI(self):
        # Set the position and size of the line edit
        self.line_edit.setGeometry(10, 10, 200, 40)
        # Set the position and size of the button
        self.button.setGeometry(210, 10, 100, 40)
        # Set the style for the line edit
        self.line_edit.setStyleSheet("font-size: 25px; font-family: Arial")
        # Set the style for the button
        self.button.setStyleSheet("font-size: 25px; font-family: Arial")
        # Set placeholder text for the line edit
        self.line_edit.setPlaceholderText("Enter your name")

        # Connect the button's click event to the submit method
        self.button.clicked.connect(self.submit)

    def submit(self):
        # Get the text from the line edit and print a greeting
        text = self.line_edit.text()
        print(f"Hello {text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application object
    window = MainWindow()  # Create an instance of the main window
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application's event loop
