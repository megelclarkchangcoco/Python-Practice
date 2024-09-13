import sys  # Import the sys module for system-specific parameters and functions
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout  # Import necessary PyQt5 widgets
from PyQt5.QtCore import QTimer, QTime, Qt  # Import core PyQt5 modules for time and alignment
from PyQt5.QtGui import QFont, QFontDatabase  # Import PyQt5 modules for font handling

class DigitalClock(QWidget):  # Define a class DigitalClock that inherits from QWidget
    def __init__(self):  # Initialize the class
        super().__init__()  # Call the parent class's constructor
        self.time_label = QLabel(self)  # Create a QLabel widget to display the time
        self.timer = QTimer(self)  # Create a QTimer object to update the time

        self.initUI()  # Call the method to initialize the user interface

    def initUI(self):  # Define the method to set up the user interface
        self.setWindowTitle("Digital Clock")  # Set the window title
        self.setGeometry(600, 400, 300, 100)  # Set the window size and position

        vbox = QVBoxLayout()  # Create a QVBoxLayout instance
        vbox.addWidget(self.time_label)  # Add the time label to the layout
        self.setLayout(vbox)  # Set the layout for the main widget

        self.time_label.setAlignment(Qt.AlignCenter)  # Center-align the text in the label

        # Set the style for the time label
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%)")
        self.setStyleSheet("background-color: black;")  # Set the background color of the window

        # Load and set a custom font for the time label
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)  # Connect the timer's timeout signal to the update_time method
        self.timer.start(1000)  # Start the timer with a 1-second interval

        self.update_time()  # Call the update_time method to set the initial time

    def update_time(self):  # Define the method to update the time
        current_time = QTime.currentTime().toString("hh:mm:ss AP")  # Get the current time as a string
        self.time_label.setText(current_time)  # Set the text of the time label to the current time

if __name__ == '__main__':  # Check if the script is being run directly
    app = QApplication(sys.argv)  # Create an instance of QApplication
    clock = DigitalClock()  # Create an instance of DigitalClock
    clock.show()  # Show the clock window
    sys.exit(app.exec_())  # Execute the application's main loop
