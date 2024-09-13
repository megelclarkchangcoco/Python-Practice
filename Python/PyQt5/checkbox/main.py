import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from PyQt5.QtCore import Qt

# Define the main window class inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the parent class (QMainWindow) constructor
        self.setGeometry(700, 300, 500, 500)  # Set the window size and position
        self.checkbox = QCheckBox("Do you like Food?", self)  # Create a checkbox widget
        self.initUI()  # Initialize the UI components

    def initUI(self):
        # Set the checkbox's position and size
        self.checkbox.setGeometry(0, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px; font-family: Arial;")  # Set the checkbox's font size and family
        self.checkbox.setChecked(False)  # Set the checkbox to be unchecked initially
        self.checkbox.stateChanged.connect(self.checkbox_changed)  # Connect the checkbox's state change event to the checkbox_changed method

    def checkbox_changed(self, state):
        # Print a message based on the checkbox's state
        if state == Qt.Checked:
            print("You Liked food")
        else:
            print("You don't like food")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application object
    window = MainWindow()  # Create an instance of the main window
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application's event loop
