🌟 Day 21 

Today I explored and implemented Counting Sort, a unique and powerful non-comparison-based sorting algorithm. Unlike Bubble Sort, Merge Sort, or Quick Sort, Counting Sort doesn’t compare elements directly. Instead, it works by counting the frequency of each element and using this information to build the sorted array.

🔹 What I Learned

Counting Sort is especially useful when:

The input elements are integers.

The range of numbers (k) is not too large compared to the number of elements (n).

Key Idea: Instead of comparing numbers pair by pair, we keep track of how many times each number appears.

Steps Involved:

Find the largest element in the array to decide the size of the count array.

Create a count array and store the frequency of each element.

Transform the count array into a cumulative count array, which tells the final position of each element.

Place elements from the original array into their correct positions in the output array (ensuring stability).

Copy the output array back to the original array.

Time Complexity:

O(n + k), where n = number of elements, k = range of input.

Space Complexity: O(n + k).

Stability: Yes ✅ (important for sorting objects with multiple keys).

🔹 Example Walkthrough

Input: [3, 6, 7, 3, 2, 4, 8]

Frequency Count → [0, 0, 1, 2, 1, 0, 1, 1, 1]

Cumulative Count → [0, 0, 1, 3, 4, 4, 5, 6, 7]

Sorted Output → [2, 3, 3, 4, 6, 7, 8]

This shows how Counting Sort processes the array step by step to reach the sorted result 🚀

🔹 Advantages

Very efficient for data with a limited range of integers.

Stable sorting algorithm.


