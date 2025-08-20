#ARRAYS

import array


arr = array.array('i', [10, 20, 30, 40, 50])
print("\nInitial Array:", arr)


print("Traversing Array Elements:")
for i in arr:
    print(i, end=" ")
print()


arr.insert(2, 99)
print("After Insertion:", arr)


arr[3] = 77
print("After Updation:", arr)


arr.remove(20)
print("After Deletion:", arr)
print("\n\n")

#LISTS


nums = [10, 20, 30, 40, 50]
print("Initial List:", nums)

print("Traversing List Elements:")
for num in nums:
    print(num,end=" ")


nums.insert(2, 25)
print("\nAfter Insertion:", nums)


nums[1] = 22
print("After Update:", nums)


nums.remove(40)
print("After Deletion:", nums)

