import threading
import multiprocessing
import time

# CPU-bound task: Calculate sum of squares for a range
def sum_of_squares(start, end, result_list=None):
    total = sum(i * i for i in range(start, end))
    if result_list is not None:
        result_list.append(total)  # Store result for threading
    return total

# Multi-threaded version (affected by GIL)
def run_with_threads(n, num_threads):
    start_time = time.time()
    threads = []
    chunk_size = n // num_threads
    results = []

    # Create threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else n
        thread = threading.Thread(target=sum_of_squares, args=(start, end, results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    total = sum(results)
    print(f"Threading: Sum of squares = {total}")
    print(f"Threading time: {time.time() - start_time:.2f} seconds")

# Multiprocessing version (bypasses GIL)
def run_with_processes(n, num_processes):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=num_processes)
    chunk_size = n // num_processes
    tasks = [(i * chunk_size, i * chunk_size + chunk_size if i < num_processes - 1 else n)
             for i in range(num_processes)]

    # Run tasks in parallel
    results = pool.starmap(sum_of_squares, tasks)
    pool.close()
    pool.join()

    total = sum(results)
    print(f"Multiprocessing: Sum of squares = {total}")
    print(f"Multiprocessing time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    n = 10_000_000  # Large range for CPU-bound work
    num_threads = 4
    num_processes = 4

    print("Running with threads (GIL-bound):")
    run_with_threads(n, num_threads)
    print("\nRunning with processes (GIL-free):")
    run_with_processes(n, num_processes)
