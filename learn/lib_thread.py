import threading
import time

def print_numbers(name, count):
    """Function to print numbers with a delay, running in a separate thread."""
    for i in range(count):
        print(f"{name} thread: {i}")
        #time.sleep(0.1)  # Simulate some work with a 1-second delay

def main():
    print("Starting the main program")
    
    # Start two threads using threading.start_new_thread
    threading._start_new_thread(print_numbers, ("Thread-1", 5))
    threading._start_new_thread(print_numbers, ("Thread-2", 5))
    
    print("Main thread continues to run")
    
    # Keep the main thread running to observe the child threads
    time.sleep(6)
    print("Main program finished")

if __name__ == "__main__":
    main()
