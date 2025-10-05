🧠 Day 25 

🚀 Topic: Bucket Sort Algorithm (Explored and Implemented)

📘 What I learned today:

Today, I explored one of the lesser-known but powerful sorting techniques — Bucket Sort. Unlike other algorithms that compare elements directly, Bucket Sort works by distributing elements into several groups called buckets. Each bucket is then sorted individually (often using another sorting method like insertion sort), and finally, all buckets are merged to get the sorted list.

This algorithm is especially useful when the data is uniformly distributed across a known range.

🔍 How it works:

Find the minimum and maximum values in the array.

Calculate the range of data and create a fixed number of buckets.

Distribute each element into its respective bucket based on a formula:

index = int(((num - min_val) / (max_val - min_val + 1)) * bucket_count)


This formula scales each number into a value between 0 and bucket_count - 1.

Sort each bucket individually.

Merge all buckets back into a single sorted list.


📊 Key Learning:

Bucket sort is non-comparative.

It’s efficient when data is spread evenly across a known range.

Formula for assigning buckets is crucial for proper distribution.

Helps understand data distribution and range normalization concepts.

🔧 Time Complexity:

Best Case: O(n + k)

Average Case: O(n + k)

Worst Case: O(n²) (when elements are unevenly distributed)
(n = number of elements, k = number of buckets)
