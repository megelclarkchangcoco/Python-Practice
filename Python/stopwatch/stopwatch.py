import sys  # Import the sys module for system-specific parameters and functions
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)  # Import necessary PyQt5 widgets
from PyQt5.QtCore import QTimer, QTime, Qt  # Import core PyQt5 modules for time and alignment

class Stopwatch(QWidget):  # Define a class Stopwatch that inherits from QWidget
    def __init__(self):  # Initialize the class
        super().__init__()  # Call the parent class's constructor
        self.time = QTime(0, 0, 0, 0)  # Initialize a QTime object to keep track of time
        self.time_label = QLabel("00:00:00.00", self)  # Create a QLabel to display the time
        self.start_button = QPushButton("Start", self)  # Create a QPushButton for starting the stopwatch
        self.stop_button = QPushButton("Stop", self)  # Create a QPushButton for stopping the stopwatch
        self.reset_button = QPushButton("Reset", self)  # Create a QPushButton for resetting the stopwatch
        self.timer = QTimer(self)  # Create a QTimer object to update the display
        self.initUI()  # Call the method to initialize the user interface

    def initUI(self):  # Define the method to set up the user interface
        self.setWindowTitle("Stopwatch")  # Set the window title

        vbox = QVBoxLayout()  # Create a QVBoxLayout instance
        vbox.addWidget(self.time_label)  # Add the time label to the vertical layout
        vbox.addWidget(self.start_button)  # Add the start button to the vertical layout
        vbox.addWidget(self.stop_button)  # Add the stop button to the vertical layout
        vbox.addWidget(self.reset_button)  # Add the reset button to the vertical layout

        self.setLayout(vbox)  # Set the layout for the main widget
        self.time_label.setAlignment(Qt.AlignCenter)  # Center-align the text in the label

        hbox = QHBoxLayout()  # Create a QHBoxLayout instance

        hbox.addWidget(self.start_button)  # Add the start button to the horizontal layout
        hbox.addWidget(self.stop_button)  # Add the stop button to the horizontal layout
        hbox.addWidget(self.reset_button)  # Add the reset button to the horizontal layout

        vbox.addLayout(hbox)  # Add the horizontal layout to the vertical layout

        # Set the style for the buttons and label
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px
            }
        """)

        # Connect the buttons to their respective methods
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)  # Connect the timer's timeout signal to the update_display method

    def start(self):  # Define the method to start the timer
        self.timer.start(10)  # Start the timer with a 10-millisecond interval

    def stop(self):  # Define the method to stop the timer
        self.timer.stop()  # Stop the timer

    def reset(self):  # Define the method to reset the timer
        self.timer.stop()  # Stop the timer
        self.time = QTime(0, 0, 0, 0)  # Reset the time to 00:00:00.00
        self.time_label.setText(self.format_time(self.time))  # Update the time label with the reset time

    def format_time(self, time):  # Define the method to format the time
        hours = time.hour()  # Get the hours from the time
        minute = time.minute()  # Get the minutes from the time
        seconds = time.second()  # Get the seconds from the time
        milliseconds = time.msec() // 10  # Get the milliseconds from the time
        return f"{hours:02}:{minute:02}:{seconds:02}:{milliseconds:02}"  # Return the formatted time string

    def update_display(self):  # Define the method to update the display
        self.time = self.time.addMSecs(10)  # Add 10 milliseconds to the time
        self.time_label.setText(self.format_time(self.time))  # Update the time label with the new time

if __name__ == "__main__":  # Check if the script is being run directly
    app = QApplication(sys.argv)  # Create an instance of QApplication
    stopwatch = Stopwatch()  # Create an instance of Stopwatch
    stopwatch.show()  # Show the stopwatch window
    sys.exit(app.exec_())  # Execute the application's main loop
