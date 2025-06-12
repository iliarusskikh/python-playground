#process vs thread
Threads:
    A thread is the smallest unit of execution within a process.
    Threads share the same memory space and resources (e.g., file handles, variables) of their parent process.

Processes:
    A process is an independent program in execution, with its own memory space, resources, and state.
    Processes are isolated from each other, meaning they don’t share memory by default.


Memory and Resource Sharing
Threads:
    Share the same memory address space, heap, and resources (e.g., open files) within the same process.
    Faster communication between threads (e.g., via shared variables).
    Risk of data corruption if threads access shared data without proper synchronization (e.g., locks).

Processes:
    Each process has its own isolated memory space and resources.
    Communication between processes (Inter-Process Communication, IPC) requires mechanisms like pipes, queues, or sockets, which are slower than thread communication.
    Safer for data integrity since processes don’t share memory by default.


Performance and Overhead
Threads:
    Lower overhead: Creating and switching between threads is faster because they share the same memory and resources.
    Uses less system memory since threads share the process’s memory.
    Better for tasks requiring frequent communication or shared data (e.g., updating a shared counter).

Processes:
    Higher overhead: Creating a process is slower due to memory allocation and resource setup.
    Consumes more memory as each process has its own copy of data and resources.
    Better for tasks requiring isolation or heavy computation (e.g., running separate instances of a program).


Parallelism
Threads:
    On a single-core CPU, threads run concurrently (via time-slicing) but not in true parallel.
    In Python, the Global Interpreter Lock (GIL) in CPython prevents true parallelism for CPU-bound tasks in threads, limiting their use for computation-heavy tasks.
    Suitable for I/O-bound tasks (e.g., network requests, file reading) where the GIL is less restrictive.
Processes:
    Can achieve true parallelism on multi-core CPUs since each process runs independently with its own Python interpreter (no GIL in Python).
    Ideal for CPU-bound tasks (e.g., data processing, machine learning) where multiple cores can be utilized.


Error Handling and Stability
Threads:
    A crash in one thread (e.g., segmentation fault) can crash the entire process, affecting all threads.
    Requires careful synchronization (e.g., locks, semaphores) to avoid race conditions or deadlocks.

Processes:
    A crash in one process doesn’t affect other processes, providing better fault isolation.
    No need for complex synchronization for shared memory, but IPC can introduce complexity.


Use Cases
Threads:
    I/O-bound tasks: Web servers, network clients, or apps waiting for user input (e.g., a Dash app handling user interactions).
    Lightweight tasks where shared memory is beneficial (e.g., updating a GUI or shared cache).
    Example: A Dash app using threads to handle concurrent user requests for real-time updates.

Processes:
    CPU-bound tasks: Heavy computations, parallel data processing, or machine learning model training.
    Isolated tasks: Running separate instances of a program or microservices.
    Example: Running multiple Dash app instances on different processes for load balancing.


Threads:
import threading
def task():
    print("Thread running")
thread = threading.Thread(target=task)
thread.start()
thread.join()

import threading
import time
def fetch_data(name):
    print(f"Fetching data for {name}")
    time.sleep(1)  # Simulate I/O wait
    print(f"Done {name}")
threads = [threading.Thread(target=fetch_data, args=(i,)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()






Processes:
from multiprocessing import Process
def task():
    print("Process running")
process = Process(target=task)
process.start()
process.join()


from multiprocessing import Process
def compute(name):
    print(f"Computing for {name}")
    sum(i * i for i in range(1000000))  # CPU-intensive
    print(f"Done {name}")
processes = [Process(target=compute, args=(i,)) for i in range(3)]
for p in processes: p.start()
for p in processes: p.join()





Use Threads if:
    Your task is I/O-bound (e.g., waiting for network responses, file I/O).
    You need lightweight concurrency within a single process.
    Shared memory simplifies your design (with proper synchronization).
    Example: Handling user interactions in a Dash app.

Use Processes if:
    Your task is CPU-bound (e.g., heavy computations).
    You need true parallelism on multiple cores.
    Isolation between tasks is critical for stability.
    Example: Running parallel computations for generating Dash graphs.
