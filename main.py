from typing import Callable, Any
from random import randint
from time import time

def kth_element(
            selector: Callable[
                [list[int], int],
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
            ):
        """
        Procedure to take place any time a selector function
        is called
        """
        start_time = time()

        chosen = selector(n, k)

        duration = time() - start_time

        print(f"({selector.__name__}) Time Taken: {duration:.8f} seconds")

        return chosen, duration

    return wrapper

def random_list_k(min_n: int, max_n: int, len: int):
    """
    Generates a random matrix of dimensions dim x dim with ints ranging from
    min_n to max_n (using the random.randint function)
    """
    return [randint(min_n, max_n) for _ in range(len)], randint(0, len-1)

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

def partition(n: list[int], start: int, end: int):
    pivot = n[end]

    i = start - 1
    for j in range(start, end):
        if n[j] <= pivot:
            i += 1
            (n[i], n[j]) = (n[j], n[i])
    (n[i + 1], n[end]) = (n[end], n[i + 1])

    return i + 1

@kth_element
def kth_merge_sort(n: list[int], k: int):
    """Uses Mergesort to sort the array then finds the kth smallest element"""
    merge_sort(n)
    return n[k-1]

@kth_element
def kth_partition(n: list[int], k: int):
    k -= 1

    start = 0
    end = len(n) - 1
    while True:
        pivot = partition(n, start, end)

        if k == pivot:
            return n[k]

        if k < pivot:
            end = pivot - 1
        else:
            start = pivot + 1
            k = k - pivot

@kth_element
def kth_mm(n: list[int], k: int):
    ...

def execute():

    n, k = random_list_k(0, 1_000, 1_000)

    for fun in [kth_merge_sort, kth_partition,]:# kth_mm]:
        print(fun(n, k)[0])

if __name__ == "__main__":
    execute()


