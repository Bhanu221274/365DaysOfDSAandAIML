def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        while i!=0:
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                if i!=0:
                    i=i-1
            else:
                i=0
    return arr

if __name__ == '__main__':
    array=[]
    n = int(input("\nEnter the number of elements: "))
    print("\n")
    for a in range(n):
        array.append(int(input(f"Enter the element at Index {a}: ")))
    print(f"\nThe array to be sorted is: {array}")
    print("\nThe sorted array is: ", Insertion_Sort(array))