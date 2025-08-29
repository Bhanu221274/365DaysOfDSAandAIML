def Selection_Sort(arr):
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

if __name__ == '__main__':
    array=[]
    n = int(input("\nEnter the number of elements: "))
    print("\n")
    for a in range(n):
        array.append(int(input(f"Enter the element at Index {a}: ")))
    print(f"\nThe array to be sorted is: {array}")
    print("\nThe sorted array is: ", Selection_Sort(array))

