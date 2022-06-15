# Compare two adjacent elements. If the first element is greater than the second element, then swap them.
# The above process goes on until we reached the last unsorted element. It's called one iteration.
# After each iteration, the largest element among the unsorted elements is placed at the end.
# So the next iteration, the comparison takes place up to the last unsorted element(1st: N, 2nd: N-1,...)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):  # 1st iteration do comparisons between[0:len(arr)-0-1], 2nd: [0: len(arr)-1-1]
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


ans = bubble_sort([3, 5, 2, 4, 1])
print(ans)

# 1. Time Complexity:
# worst case: O(N^2)  The array is reversed-sorted.
# best case: O(N)
# 2. Space Complexity: O(1)
# 3. Stability: Yes, insertion sort preserve the relative order of items with equal keys.


