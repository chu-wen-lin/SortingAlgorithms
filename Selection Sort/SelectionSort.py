# In each iteration,
# 1. Selects the smallest element from an unsorted list
# 2. Swap the smallest element for the beginning element of the unsorted list.

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i   # the index of smallest element

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


ans = selection_sort([1, 5, 3, 8, 2])
print(ans)

# 1. Time Complexity: O(N^2)
# Time complexity of selection sort is the same in all cases.
# At each iteration, we have to find the minimum element.
# While the minimum element is unknown until the end of the array is reached.
# 2. Space Complexity: O(1)
# 3. Stability: NO!
# B1 B2 A1 -> Swap B1 for A1, then we get A1 B2 B1. The next iteration we find B1 == B2, so it remains to be A1 B2 B1
