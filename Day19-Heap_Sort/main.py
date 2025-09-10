def heapify(tree, size, root_index):
    largest_index = root_index
    left_child_index = 2 * root_index + 1
    right_child_index = 2 * root_index + 2

    if left_child_index < size and tree[left_child_index] > tree[largest_index]:
        largest_index = left_child_index

    if right_child_index < size and tree[right_child_index] > tree[largest_index]:
        largest_index = right_child_index

    if largest_index != root_index:
        tree[root_index], tree[largest_index] = tree[largest_index], tree[root_index]
        heapify(tree, size, largest_index)


def heap_sort(tree):
    total_nodes = len(tree)

    for node_index in range(total_nodes // 2 - 1, -1, -1):
        heapify(tree, total_nodes, node_index)

    for end_index in range(total_nodes - 1, 0, -1):
        tree[0], tree[end_index] = tree[end_index], tree[0]
        heapify(tree, end_index, 0)
        
    return tree


if __name__ == '__main__':
    array=[]
    n = int(input("\nEnter the number of elements: "))
    print("\n")
    for a in range(n):
        array.append(int(input(f"Enter the element at Index {a}: ")))
    print(f"\nThe array to be sorted is: {array}")
    print("\nThe sorted array is: ", heap_sort(array))

