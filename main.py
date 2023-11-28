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

def kth_sort(n: list[int], k: int):
    """Uses Mergesort to sort the array then finds the kth smallest element"""
    merge_sort(n)
    return n[k-1]

def execute():

    print(kth_sort([10, 2, 4, 6, 3, 2,5 , 62, 5, 6, 3,2 , 5], 6))


if __name__ == "__main__":
    execute()


