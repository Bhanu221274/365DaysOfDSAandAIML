
import numpy as np
def linear_search(arr, targ):

    for i in range(len(arr)):
        if arr[i] == targ:
            return i
    return -1



array = np.array([10, 25, 7, 30, 15])
target = 30

result = linear_search(array, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
