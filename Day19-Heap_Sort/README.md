Day 19 – Heap Sort ⚡

🔹 What I Learned

- Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.

- It first builds a Max-Heap so that the largest element is at the root.

- Then, the root is swapped with the last element, the heap size is reduced, and heapify is applied again.

- This process repeats until the array is sorted.

- Time Complexity: O(n log n) (best, average, worst).

- Space Complexity: O(1) (in-place sorting).

- Heap Sort guarantees stable performance, unlike Quick Sort which can degrade to O(n²) in worst cases.

🔹 Implementation

- Implemented heapify to maintain the Max-Heap property.

- Built Max-Heap from an unsorted array.

- Repeatedly swapped the root with the last element and heapified the reduced heap.

Sorted the array in ascending order.
