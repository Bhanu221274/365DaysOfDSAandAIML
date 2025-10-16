Day 27: Shell Sort

🔹 What I Learned

Shell Sort is an advanced version of Insertion Sort that works more efficiently by comparing elements far apart.

It starts with a large gap between elements and reduces the gap after each pass.

Sorting with larger gaps first moves elements closer to their final position, making the later passes faster.

Final pass works like a normal Insertion Sort when the gap becomes 1.

Time complexity depends on the chosen gap sequence, generally better than O(n²).

It’s an in-place sorting algorithm and doesn’t need extra memory.

🔹 Algorithm Steps

Choose an initial gap (usually n//2).

Compare elements at that gap and sort them.

Reduce the gap and repeat.

Continue until the gap becomes 1.

🧠 Why it’s useful

Faster than simple sorting algorithms like Bubble or Insertion Sort.

Easy to implement.

Performs well on medium-sized datasets.
