import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

# Define the main window class inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the parent class (QMainWindow) constructor
        self.setGeometry(700, 300, 500, 500)  # Set the window size and position
        self.button = QPushButton("Click me!", self)  # Create a button widget
        self.label = QLabel("Hello", self)  # Create a label widget
        self.initUI()  # Initialize the UI components

    def initUI(self):
        # Set the button's position and size
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 15px;")  # Set the button's font size
        self.button.clicked.connect(self.on_click)  # Connect the button's click event to the on_click method
https://github.com/megelclarkchangcoco/Python-Practice/tree/main/Python
        # Set the label's position and size
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 15px;")  # Set the label's font size

    def on_click(self):
        # Change the label's text when the button is clicked
        self.label.setText("Love u Liza!")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application object
    window = MainWindow()  # Create an instance of the main window
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application's event loop
