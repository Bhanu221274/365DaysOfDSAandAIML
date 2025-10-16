def shell_sort(numbers):
    size = len(numbers)
    gap = size // 2

    while gap > 0:
        for current in range(gap, size):
            value_to_insert = numbers[current]
            position = current

            while position >= gap and numbers[position - gap] > value_to_insert:
                numbers[position] = numbers[position - gap]
                position -= gap

            numbers[position] = value_to_insert
        gap //= 2


    return numbers

if __name__ == '__main__':
    array=[]
    n = int(input("\nEnter the number of elements: "))
    print("\n")
    for a in range(n):
        array.append(int(input(f"Enter the element at Index {a}: ")))
    print(f"\nThe array to be sorted is: {array}")
    print("\nThe sorted array is: ", shell_sort(array))
