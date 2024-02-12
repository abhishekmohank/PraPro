import time
import numpy as np

# Measure the time it takes to create a 1000x1000 random numpy array

start_time = time.time()
random_array = np.random.rand(1000, 1000)
creation_time = time.time() - start_time

# Convert the array into bytes

bytes_array = random_array.tobytes()

# Measure the time it takes to recreate the array from bytes

start_time = time.time()
recreated_array = np.frombuffer(bytes_array, dtype=random_array.dtype).reshape(random_array.shape)
recreation_time = time.time() - start_time

# Print the times

print(f"Array creation time: {creation_time:.6f} seconds")
print(f"Array recreation time: {recreation_time:.6f} seconds")

## we use np.random.rand to create a 1000x1000 random numpy array.
## We then measure the time it takes for both the array creation and recreation 
## from bytes using the time package. 
## The tobytes method is used to convert the array into bytes, and np.frombuffer is used to recreate the array from the bytes.




