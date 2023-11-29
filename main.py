from typing import Callable, Any
from random import randint
from time import time
from math import ceil

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
                *args: Any
            ):
        """
        Procedure to take place any time a selector function
        is called
        """
        start_time = time()

        chosen = selector(n, k, *args)

        duration = time() - start_time

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
    pivot = pivot or n[end]

    i = start - 1
    for j in range(start, end):
        if n[j] <= pivot:
            i += 1
            (n[i], n[j]) = (n[j], n[i])
    (n[i + 1], n[end]) = (n[end], n[i + 1])

    return i + 1

def find_median(n: list[int]):
    n_c = [i for i in n]
    merge_sort(n_c)
    return n_c[len(n)//2]

def median_medians(a: list[int], r: int = 5):
    if len(a) < r*r:
        return find_median(a)

    subn = [a[i:i+r] for i in range(0, len(a), r) if i + r <= len(a)]
    print(subn)
    medians = [find_median(sub) for sub in subn]
    print(medians)
    return find_median(medians)

@kth_element
def kth_merge_sort(n: list[int], k: int):
    """Uses Mergesort to sort the array then finds the kth smallest element"""
    merge_sort(n)
    return n[k-1]

@kth_element
def kth_partition(n: list[int], k: int):
    """"""
    k -= 1

    start = 0
    end = len(n) - 1
    while True:

        if (start >= end):
            return n[start]

        pivot_pos = partition(n, start, end)
        if k == pivot_pos:
            return n[k]

        if k < pivot_pos:
            end = pivot_pos - 1
        else:
            start = pivot_pos + 1

@kth_element
def kth_mm(n: list[int], k: int):
    """"""
    k -= 1

    start = 0
    end = len(n) - 1
    while True:

        if (start >= end):
            return n[start]

        pivot_pos = median_medians(n[start:end])
        if k == pivot_pos:
            return n[k]

        if k < pivot_pos:
            end = pivot_pos - 1
        else:
            start = pivot_pos + 1

def execute():

    # n, k = random_list_k(0, 10, 10)

    n = [7, 0, 4, 1, 7, 7, 7, 7, 9, 6]
    k = 2

    print(median_medians(n))

    # print("------")
    # print(n, k)
    # print("------")

    # kth_merge_sort([i for i in n], k)
    # kth_partition([i for i in n], k)
    # kth_mm([i for i in n], k)
    # kth_mm([i for i in n], k)

if __name__ == "__main__":
    execute()


