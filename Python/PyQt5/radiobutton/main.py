import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

# Define the main window class inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the parent class (QMainWindow) constructor
        self.setGeometry(700, 300, 300, 500)  # Set the window size and position
        self.radio1 = QRadioButton("Visa", self)  # Create a radio button for "Visa"
        self.radio2 = QRadioButton("Mastercard", self)  # Create a radio button for "Mastercard"
        self.radio3 = QRadioButton("Gift Card", self)  # Create a radio button for "Gift Card"
        self.radio4 = QRadioButton("In-Store", self)  # Create a radio button for "In-Store"
        self.radio5 = QRadioButton("Online", self)  # Create a radio button for "Online"
        self.button_group1 = QButtonGroup(self)  # Create a button group for the first set of radio buttons
        self.button_group2 = QButtonGroup(self)  # Create a button group for the second set of radio buttons
        self.initUI()  # Initialize the UI components

    def initUI(self):
        # Set the position and size of the radio buttons
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # Set the style for the radio buttons
        self.setStyleSheet("QRadioButto{"
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")

        # Add the radio buttons to their respective button groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Connect the toggled signal of each radio button to the radio_button_changed method
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        # Get the radio button that triggered the event
        radio_button = self.sender()
        # Check if the radio button is checked and print its text
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application object
    window = MainWindow()  # Create an instance of the main window
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application's event loop
