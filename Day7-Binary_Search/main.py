def BinarySearch(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Element {target} was found at index {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"Element {target} not found"

if __name__ == "__main__":
    arr = []
    no_of_elements = int(input("Enter the number of elements: "))
    print("\n")
    for i in range(no_of_elements):
        n = int(input(f"Enter the element at index {i}: "))
        arr.append(n)

    arr.sort()
    print(f"\nThe Sorted Array is : {arr}")

    target = int(input("\nEnter the element to be found: "))
    print(f"\n{BinarySearch(arr, target)}")
