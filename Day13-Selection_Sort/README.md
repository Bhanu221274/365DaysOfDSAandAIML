📘 Day 13 – Selection Sort (DSA)

🔹 What is Selection Sort?

Selection Sort is a simple sorting algorithm where we repeatedly pick the smallest element from the unsorted portion of the list and place it at the correct position.

🔹 How it Works (Step by Step Example)

Array = [4, 2, 6, 1, 8, 5]

Pass 1: Find smallest in [4,2,6,1,8,5] → 1, swap with 4 → [1,2,6,4,8,5]

Pass 2: Smallest in [2,6,4,8,5] → 2, already in place → [1,2,6,4,8,5]

Pass 3: Smallest in [6,4,8,5] → 4, swap with 6 → [1,2,4,6,8,5]

Pass 4: Smallest in [6,8,5] → 5, swap with 6 → [1,2,4,5,8,6]

Pass 5: Smallest in [8,6] → 6, swap with 8 → [1,2,4,5,6,8]

✅ Final Sorted Array: [1, 2, 4, 5, 6, 8]


🔹 Time & Space Complexity

Time Complexity

Best case: O(n²)

Worst case: O(n²)

Average case: O(n²)

Space Complexity: O(1) → No extra space, done in-place

🔹 Key Notes

Very easy to understand for beginners.

Not efficient for large datasets (O(n²) comparisons).

Useful when simplicity is more important than performance.

