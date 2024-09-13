# PyQt5 Introduction
# Import the sys module to handle command-line arguments
import sys
# Import QApplication and QMainWindow from PyQt5.QtWidgets for creating the application and main window
from PyQt5.QtWidgets import QApplication, QMainWindow
# Import QIcon from PyQt5.QtGui to set the window icon
from PyQt5.QtGui import QIcon

# Define a class MainWindow that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        # Call the constructor of the parent class QMainWindow
        super().__init__()
        # Set the title of the window
        self.setWindowTitle("My cool first GUI")
        # Set the position and size of the window (x, y, width, height)
        self.setGeometry(700, 300, 500, 500)
        # Set the window icon using an image file
        self.setWindowIcon(QIcon("mylove.jpg"))

# Define the main function to run the application
def main():
    # Create an instance of QApplication, passing command-line arguments
    app = QApplication(sys.argv)
    # Create an instance of MainWindow
    window = MainWindow()
    # Show the main window
    window.show()
    # Execute the application's main loop
    sys.exit(app.exec_())

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the application
    main()






