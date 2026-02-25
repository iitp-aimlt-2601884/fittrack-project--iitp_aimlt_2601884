# task 1 - Create an Array and Basic Math
import numpy as np

temps_celsius = np.array([22,25,28,24,26])
temps_fahernheit = temps_celsius * 1.8 + 32
temps_avg_fahrenheit = np.mean(temps_fahernheit)

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahernheit)
print("Average Fahrenheit:", temps_avg_fahrenheit)

# task 2 - Array Shape and Statistics
test_scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape:", test_scores.shape)
print("Total elements:", test_scores.size)
print("Highest score:", np.max(test_scores))
print("Lowest score:", np.min(test_scores))
print("Range:", np.ptp(test_scores))

# task 3 - Performance Comparison
import time
numpy_arr = np.arange(1, 50001)
python_arr = list(range(1, 50001))

start_time = time.time()
numpy_sum = np.sum(numpy_arr)
numpy_time = time.time() - start_time   

start_time = time.time()
python_sum = sum(python_arr)
python_time = time.time() - start_time

speed = python_time / numpy_time

print("Numpy sum:", numpy_sum)
print("Python sum:", python_sum)
print("Numpy time:", f"{numpy_time:.4f} seconds")
print("Python time:", f"{python_time:.4f} seconds")
print("NumPy is ", f"{speed:.1f}x faster")
