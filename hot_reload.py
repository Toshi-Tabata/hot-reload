import time
import os
import sys
import threading


# Function for restarting the current file's scripts whenever the file is modified
def restart():

    # How often to check for file changes
    sleep_length = 2

    # Get the last time this file was modified
    last_modified = os.path.getmtime(__file__)

    # Check for changes in the current file
    while True:
        time.sleep(sleep_length)
        if os.path.getmtime(__file__) > last_modified:
            print("restarting")
            os.execv(sys.executable, ["python", __file__])


if __name__ == "__main__":

    # Create a thread to start checking
    t = threading.Thread(target=restart)
    t.start()

    # Example of a Main function loop
    while True:
        print("hihi")
        time.sleep(10)
