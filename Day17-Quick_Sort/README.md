Day 17 – Quick Sort ⚡

🔹 What I Learned

- Quick Sort is a divide and conquer algorithm used for sorting.

- It works by:

   - Choosing a pivot element.

   - Partitioning the array into two parts:
      • Elements smaller than pivot → left side.
      • Elements greater than pivot → right side.

   - Recursively sorting the left and right subarrays.

- Unlike Merge Sort, Quick Sort does not need extra arrays for merging, making it more space-efficient.

- Time Complexity:

   - Best / Average Case → O(n log n)

   - Worst Case → O(n²) (when pivot choice is poor, e.g., already sorted array).

- Space Complexity: O(log n) (due to recursion).

🔹 Example

Input Array: [8, 3, 1, 7, 0, 10, 2]

Steps:

Pivot = 2, partition → [0, 1] [2] [8, 3, 7, 10]

Recursively sort left & right → [0, 1, 2, 3, 7, 8, 10].
