⭐ Day 11 – Insertion Sort ⭐

📌 What I Learned

- Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time.

- It works by taking an element from the unsorted portion and placing it into the correct position in the sorted portion.

- Think of it like sorting playing cards in your hand: pick a card, place it in the right position among the cards you already hold.

- Sorting is done in-place, so no extra memory is needed.

🔹 Step-by-Step Example

- Array to sort:

    [5, 3, 4, 1, 2]


- Compare 3 with 5 → swap → [3, 5, 4, 1, 2]

- Compare 4 with 5 → swap → [3, 4, 5, 1, 2]

- Compare 1 with 5, 4, 3 → shift all → [1, 3, 4, 5, 2]

- Compare 2 with 5, 4, 3 → shift all → [1, 2, 3, 4, 5]

- ✅ Final sorted array: [1, 2, 3, 4, 5]

⏳ Time Complexity

- Best Case (already sorted): O(n) → only one comparison per element

- Worst Case (reverse sorted): O(n²) → maximum comparisons and shifts

- Average Case: O(n²)

🗂 Space Complexity

- O(1) → sorting is done in-place with a single temporary variable
