def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int(((num - min_val) / (max_val - min_val + 1)) * bucket_count)
        buckets[index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


if __name__ == '__main__':
    array=[]
    n = int(input("\nEnter the number of elements: "))
    print("\n")
    for a in range(n):
        array.append(int(input(f"Enter the element at Index {a}: ")))
    print(f"\nThe array to be sorted is: {array}")
    print("\nThe sorted array is: ", bucket_sort(array))