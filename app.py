import matplotlib.pyplot as plt
import numpy as np
import time
import random

# Quick Sort implementation [O(n log n)]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Insertion Sort implementation [O(n^2)]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Measure the time taken to sort the array using a given sort function
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Define n values (from 0 to 50,000, incrementing by 10,000)
n_values = np.arange(0, 50001, 10000)

# Initialize lists to store timing results
quick_sort_times = []
insertion_sort_times = []

# Perform sorting and measure times
for n in n_values:
    # Generate random data of size n
    test_data = [random.randint(0, 100000) for _ in range(n)]
    
    # Measure time for Quick Sort
    quick_sort_times.append(measure_time(quick_sort, test_data.copy()))  # Use .copy() to avoid sorting already sorted data
    
    # Measure time for Insertion Sort
    insertion_sort_times.append(measure_time(insertion_sort, test_data.copy()))

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot(n_values, quick_sort_times, label='Quick Sort (Actual Time)', marker='o')

# Plotting Insertion Sort
plt.plot(n_values, insertion_sort_times, label='Insertion Sort (Actual Time)', marker='o')

# Add labels and title
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quick Sort vs Insertion Sort')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
