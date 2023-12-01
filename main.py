from typing import Callable, Any
from random import randint
from time import time

def kth_element(
            selector: Callable[
                [list[int], int, Any],
                int
            ]
        ):
    """
    A decorator for a function taking a list and an index
    to return the indexth smallest element
    """

    def wrapper(
                n: list[int],
                k: int,
                *args: Any,
                root_call: bool = True
            ):
        """
        Procedure to take place any time a selector function
        is called
        """
        start_time = time()

        if root_call:
            k -= 1

        chosen = selector(n, k, *args)

        duration = time() - start_time

        if root_call:
            print(f"({selector.__name__}) | Time Taken: {duration:.4f} seconds | Selected: {chosen}")

        return chosen, duration

    return wrapper

def random_list_k(min_n: int, max_n: int, len: int):
    """
    Generates a random matrix of dimensions dim x dim with ints ranging from
    min_n to max_n (using the random.randint function)
    """
    return [randint(min_n, max_n) for _ in range(len)], randint(1, len-1)

def merge_sort(n: list[int]):
    if len(n) <= 1:
        return

    mid = len(n) // 2
    left = n[:mid]
    right = n[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            n[k] = left[i]
            i += 1
        else:
            n[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        n[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        n[k] = right[j]
        j += 1
        k += 1

def partition(n: list[int], start: int, end: int, pivot: int | None = None):
    if pivot is not None:
        switch_index = n.index(pivot)
        n[switch_index], n[end - 1] = n[end - 1], n[switch_index]
    else:
        pivot = n[end - 1]

    i = start
    for j in range(start, end):
        if n[j] < pivot:
            n[i], n[j] = n[j], n[i]
            i += 1

    (n[i], n[end-1]) = (n[end-1], n[i])

    return i

def find_median(n: list[int]):
    merge_sort(n)
    return n[len(n)//2]

def median_of_medians(n: list[int], start: int, end: int, r: int = 5):
    if len(n) < r * r:
        return find_median(n)

    sublists = [n[i:i+r] for i in range(start, end+1, r) if i + r < len(n)]
    medians = [find_median(sublist) for sublist in sublists]

    return find_median(medians)

@kth_element
def kth_merge_sort(n: list[int], k: int):
    """Uses Mergesort to sort the array then finds the kth smallest element"""
    merge_sort(n)
    return n[k]

@kth_element
def kth_partition(n: list[int], k: int, start: int = 0, end: int | None = None):
    """"""
    if end is None:
        end = len(n)

    pivot_pos = partition(n, start, end)

    if k == pivot_pos:
        return n[pivot_pos]

    if k < pivot_pos:
        return kth_partition(n, k, start, pivot_pos, root_call=False)[0]

    return kth_partition(n, k, pivot_pos + 1, end, root_call=False)[0]

@kth_element
def kth_mm(n: list[int], k: int, start: int = 0, end: int | None = None):
    """"""
    if end is None:
        end = len(n)

    pivot = median_of_medians(n, start, end)
    pivot_pos = partition(n, start, end, pivot)

    if k == pivot_pos:
        return n[pivot_pos]

    if k < pivot_pos:
        return kth_mm(n, k, start, pivot_pos, root_call=False)[0]

    return kth_mm(n, k, pivot_pos + 1, end, root_call=False)[0]

def execute():

    # while True:
    n, k = random_list_k(0, 15, 15)

    # n = [5, 3, 7, 2, 8, 1]
    # k = 4
    print(sorted(n))

    # print(partition(n, 0, len(n)))
    # print(n)

    # print(partition(n, 0, len(n)), 3)
    # print(n)

    print("------")
    print(n, k)
    print("------")

    kth_merge_sort([i for i in n], k)[0]
    kth_partition([i for i in n], k)[0]
    kth_mm([i for i in n], k)[0]

if __name__ == "__main__":
    execute()


