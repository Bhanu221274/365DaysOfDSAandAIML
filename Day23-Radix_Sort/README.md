Day 24 – Radix Sort 🔢


🔹 What I Learned

Radix Sort is a non-comparison-based sorting algorithm.

It sorts numbers by processing individual digits from the least significant digit (LSD) to the most significant digit (MSD).

Instead of comparing elements directly (like Quick Sort or Merge Sort), it uses digit places and a stable sort (often Counting Sort) to order numbers step by step.

Example: Sorting [987, 46, 90, 1, 23, 0, 56] →

First sort by the units digit.

Then sort by the tens digit.

Finally sort by the hundreds digit.

After processing all digits, the entire list becomes sorted.

Key Points

Time Complexity:

Best/Average/Worst → O(n·k), where n = number of elements and k = number of digits.

Since k is usually small, Radix Sort can be very efficient.

Space Complexity: O(n + k).

Stability: Radix Sort is stable if the intermediate sorting algorithm (like Counting Sort) is stable.

Limitation: Works best for integers or fixed-length strings. Not useful for floating numbers or very large ranges without modification.

🔹 Implementation Steps

Find the maximum number → Decide the number of digits we need to process.

Normalize numbers → Add leading zeros to make all numbers have equal length.

Sort digit by digit → Use a stable sort like Counting Sort for each digit position.

Repeat until all digit places are processed → Final list is fully sorted.

🔹 Example Walkthrough

Array = [987, 46, 90, 1, 23, 0, 56]

Step 1: Equalize length → [987, 046, 090, 001, 023, 000, 056]

Step 2: Sort by units place → [000, 001, 090, 023, 046, 056, 987]

Step 3: Sort by tens place → [000, 001, 987, 090, 023, 046, 056]

Step 4: Sort by hundreds place → [000, 001, 023, 046, 056, 090, 987]

✅ Final Sorted Output = [0, 1, 23, 46, 56, 90, 987]
