# multithreading = used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

# Import the threading module to create and manage threads
import threading

# Import the time module to use sleep function
import time

# Define a function to simulate walking the dog
def walk_dog(first, last):
    time.sleep(8)  # Simulate the time taken to walk the dog by sleeping for 8 seconds
    print(f"You finish walking {first} {last}")  # Print a message when done

# Define a function to simulate taking out the trash
def take_out_trash():
    time.sleep(2)  # Simulate the time taken to take out the trash by sleeping for 2 seconds
    print("You take out the trash")  # Print a message when done

# Define a function to simulate getting the mail
def get_mail():
    time.sleep(4)  # Simulate the time taken to get the mail by sleeping for 4 seconds
    print("You get the mail")  # Print a message when done

# Create a thread to run the take_out_trash function
chore1 = threading.Thread(target=take_out_trash)
# Start the thread
chore1.start()

# Create a thread to run the get_mail function
chore2 = threading.Thread(target=get_mail)
# Start the thread
chore2.start()

# Create a thread to run the walk_dog function with arguments "Scooby" and "Doo"
chore3 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
# Start the thread
chore3.start()

# Wait for chore1 thread to complete
chore1.join()
# Wait for chore2 thread to complete
chore2.join()
# Wait for chore3 thread to complete
chore3.join()

# Print a message indicating all chores are complete
print("All Chores are complete")
