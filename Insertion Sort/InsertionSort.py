# Imagine how you sort cards in your hand in a card game!

from typing import List


def insertion_sort(arr: List[int]):   # or List[str] if we want to sort alphabetically
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1

        while j >= 0 and cur < arr[j]:  # compare with each element on the left until a smaller element is found
            arr[j+1] = arr[j]  # move element(which is equal or bigger than cur)back
            j -= 1
        arr[j+1] = cur  # arr[j] is smaller than cur, so we place cur right after arr[j]

    return arr


ans = insertion_sort([3, 7, 2, 1])
print(ans)

# 1. Time Complexity:
# worst case: O(N^2)  The array is reversed-sorted.
# best case: O(N) When the array is already sorted, the outer loop runs for n times whereas the inner loop does not run at all.
# 2. Space Complexity: O(1)
# 3. Stability: Yes, insertion sort preserve the relative order of items with equal keys.
