def counting_sort(arr):
    largest = 0
    for i in arr:
        if i > largest:
            largest = i

    count = [0 for i in range(largest+1)]

    for j in range(len(count)):
        for i in range(len(arr)):
            if arr[i] == j:
                count[j] += 1

    for z in range(1, len(count)):
        count[z] = count[z] + count[z-1]

    output = [0] * len(arr)

    for i in range(len(arr)-1, -1, -1):
        current = arr[i]
        position = count[current] - 1
        output[position] = current
        count[current] -= 1

    return output

if __name__ == '__main__':
    array=[]
    n = int(input("\nEnter the number of elements: "))
    print("\n")
    for a in range(n):
        array.append(int(input(f"Enter the element at Index {a}: ")))
    print(f"\nThe array to be sorted is: {array}")
    print("\nThe sorted array is: ", counting_sort(array))






