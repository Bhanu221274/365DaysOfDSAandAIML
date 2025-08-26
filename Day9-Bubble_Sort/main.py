def Bubble_Sort(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

if __name__ == '__main__':
    arr=[]
    n = int(input("\nEnter the number of elements: "))
    print("\n")
    for i in range(n):
        arr.append(int(input(f"Enter the element at Index {i}: ")))
    print(f"\nThe array to be sorted is: {arr}")
    print("\nThe sorted array is: ", Bubble_Sort(arr))