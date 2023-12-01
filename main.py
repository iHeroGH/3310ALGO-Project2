from typing import Callable, Any, Optional
from random import randint
from time import time
from matplotlib import pyplot as plt

### MISC. HELPERS
def kth_element(
            selector: Callable[
                [list[int], int],
                int
            ],
        ) -> Callable[[list[int], int, Any, bool], tuple[int, float]]:
    """
    A decorator for a function taking a list and an index
    to return the indexth smallest element

    Parameters
    ----------
    selector: Callable[list[int], int], int
        A `selector` function is a function that takes a list of integers and
        a target to select, and returns an integer.

    Returns
    -------
    Callable[[list[int], int, Any, bool], tuple[int, float]]:
        The `selector` callable wrapper. Takes the list and target inputs as
        well as any number of additional arguments (like `start` or `end`) and
        a boolean denoting whether or not this is the root_call (as opposed to
        a recursive call). This function will return a tuple of the selected
        element and the time taken to retrieve it
    """

    def wrapper(
                n: list[int],
                k: int,
                *args: Any,
                root_call: bool = True
            ) -> tuple[int, float]:

        """
        Procedure to take place any time a selector function is called.

        Times the called selector and prints the time it took and its selected
        value (descriptor string)

        Parameters
        ----------
        n: list[int]
            The list to find the kth smallest element for
        k: int
            The target smallest element to find
        *args: Any
            Any additional arguments this selector may need
        root_call: bool = True
            A boolean denoting whether or not this is the root call
            (as opposed to a recursive call). Used to prevent descriptor
            string from printing for every recursive call

        Returns
        -------
        tuple[int, float]:
            A tuple of the selected value and the time taken to select
        """

        # Start timing
        start_time = time()

        # Lists are 0-indexed, but we want k to be human-readable
        # "The 1st smallest element"
        # So we translate it from 1-indexed
        if root_call:
            k -= 1

        # Call the selector
        chosen = selector(n, k, *args)

        # Stop timing and print some info if this isn't a recursive call
        duration = time() - start_time

        if root_call:
            print(
                f"({selector.__name__}) | " +
                f"Time Taken: {duration:.4f} seconds | Selected: {chosen}"
            )

        return chosen, duration

    return wrapper

def random_list_k(min_n: int, max_n: int, len: int) -> tuple[list[int], int]:
    """
    Generates a list of random numbers between min_n and max_n, including both
    end points, of size len. Also generates a random number between 1 and the
    length

    Parameters
    ----------
    min_n: int
        The minimum number to generate
    max_n: int
        The maximum number to generate
    len: int
        The length of list to generate

    Return
    ------
    tuple[list[int], int]:
        A tuple of the list generated and the random selection target
    """
    return [randint(min_n, max_n) for _ in range(len)], randint(1, len-1)

def selection_equality(*selected: int) -> bool:
    """
    Ensures that all integer positional arguments passed are equal

    Parameters
    ----------
    *selected: int
        The integers to check

    Returns
    -------
    bool:
        Whether or not the arguments are all the same
    """
    if not selected:
        return True

    # Compare every element in `selected` to the first element
    first = selected[0]
    for selection in selected:
        if not first == selection:
            return False

    return True

### ALGO 1 HELPER
def merge_sort(n: list[int]) -> None:
    """
    Sorts the given list, updating the input list (does not return a new list),
    using merge sort

    Parameters
    ----------
    n: list[int]
        The integer list to sort
    """

    # Base case: a list of length 1 is already sorted
    if len(n) <= 1:
        return

    mid = len(n) // 2
    left = n[:mid]
    right = n[mid:]

    # Recursive calls
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    # Compare left and right and choose the lower value
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            n[k] = left[i]
            i += 1
        else:
            n[k] = right[j]
            j += 1
        k += 1

    # Fill in the remaining elements
    while i < len(left):
        n[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        n[k] = right[j]
        j += 1
        k += 1

### ALGO 2 HELPER
def partition(
            n: list[int], start: int, end: int, pivot: int | None = None
        ) -> int:
    """
    Applies the quicksort partition procedure on the given list.

    All elements less than the pivot will be to the left of the pivot (not
    necessarily in order). All elements greater than the pivot will be to the
    right of the pivot (not necessarily in order).

    Regardless, the pivot itself will be in its final, sorted, position (in
    reference to the start and end positions given).

    The start and end parameters are used to constrict the function to only
    examine elements within n[start:end], but the entire list is provided
    to accurately determine the pivot index at the end.

    Parameters
    ----------
    n: list[int]
        The list to apply the procedure to
    start: int
        The starting index to examine
    end: int
        The ending index to exmaine
    pivot: int | None = None
        If provided, this will be used as the pivot, and will be sorted by the
        end of the procedure within the start-end bounds of the array. If not
        provided, the element at the end index will be used as the pivot.

    Returns
    -------
    int:
        The index of the pivot used. The pivot is in its sorted spot, therefore
        this index is the index of a sorted item and can be used justly.
    """

    # If a pivot is provided, get its index and swap it with the last element
    # to be consistent with the rest of the function
    if pivot is not None:
        switch_index = n[start:end].index(pivot) + start
        n[switch_index], n[end - 1] = n[end - 1], n[switch_index]
    else:
        pivot = n[end - 1]

    # Swap elements accordingly
    i = start
    for j in range(start, end):
        if n[j] < pivot:
            n[i], n[j] = n[j], n[i]
            i += 1

    (n[i], n[end-1]) = (n[end-1], n[i])

    return i

### ALGO 3 HELPER
def find_median(n: list[int]) -> int:
    """
    Simply finds the middle element of the given list. This uses the pre-defined
    `merge_sort` function to sort the list in place.

    Parameters
    ----------
    n: list[int]
        The list to retrieve the median of

    Returns
    -------
    int:
        The middle element of the list
    """
    merge_sort(n)
    return n[len(n)//2]

def median_of_medians(n: list[int], r: int = 5) -> int:
    """"
    Finds the median of the median of the given list. This point has a special
    property; it is able to be used to guarantee the removal of significant
    portions of the problem size for the kth-smallest element algorithm.

    Parameters
    ----------
    n: list[int]
        The list to find median of medians for
    r: int = 5
        The length of the sublists

    Returns
    -------
    int:
        The median of medians for the given list
    """

    # Base case: we don't have enough elements to create the necessary sublists
    if len(n) < r * r:
        return find_median(n)

    # Create at least r sublists of length r
    sublists = [n[i:i+r] for i in range(0, len(n), r)]
    # The median of each sublist
    medians = [find_median(sublist) for sublist in sublists]

    # The median... of the medians... of the sublists haha :(
    return median_of_medians(medians, r)

### SELECTION METHODS
@kth_element
def kth_merge_sort(
            n: list[int], k: int
        ) -> int:
    """
    Uses `merge_sort` to sort the array then finds the kth smallest element

    Parameter
    ---------
    n: list[int]
        The list to find the kth smallest element for
    k: int
        The target smallest element to find

    Returns
    -------
    int:
        The k-th smallest element
    """
    merge_sort(n)
    return n[k]

@kth_element
def kth_partition(
            n: list[int], k: int, start: int = 0, end: int | None = None
        ) -> int:
    """
    Uses `partition` to procedurally sort the found pivot points and find
    the kth-smallest element. Terminates early if the kth-smallest element
    is found before the list is fully sorted.

    Parameter
    ---------
    n: list[int]
        The list to find the kth smallest element for
    k: int
        The target smallest element to find
    start: int = 0
        The starting index to begin partitioning from
    end: int | None = None
        The ending index to end partitioning from. If not provided,
        the length of the input list will be used

    Returns
    -------
    int:
        The k-th smallest element
    """

    # Default to length of n. Since this is an expression, it cannot be
    # used in the function header
    if end is None:
        end = len(n)

    # Procedurally sort the array and find the sorted position of the pivot
    pivot_pos = partition(n, start, end)

    # We found the kth-smallest element
    if k == pivot_pos:
        return n[pivot_pos]

    # kth-smallest element is in the left sublist (restrict end to pivot)
    if k < pivot_pos:
        return kth_partition(n, k, start, pivot_pos, root_call=False)[0] # type: ignore

    # kth-smallest element is in the right sublist (restrict start to pivot + 1)
    return kth_partition(n, k, pivot_pos + 1, end, root_call=False)[0] # type: ignore

@kth_element
def kth_mm(
            n: list[int], k: int, start: int = 0, end: int | None = None
        ) -> int:
    """
    Uses `median_of_medians` to find a more effecient pivot point then uses
    `partition` to procedurally sort the found pivot points and find the
    kth-smallest element. Terminates early if the kth-smallest element
    is found before the list is fully sorted.

    Parameter
    ---------
    n: list[int]
        The list to find the kth smallest element for
    k: int
        The target smallest element to find
    start: int = 0
        The starting index to begin partitioning from
    end: int | None = None
        The ending index to end partitioning from. If not provided,
        the length of the input list will be used

    Returns
    -------
    int:
        The k-th smallest element
    """

    # Default to length of n. Since this is an expression, it cannot be
    # used in the function header
    if end is None:
        end = len(n)

    # The pivot is found using median_of_medians
    # Procedurally sort the array and find the sorted position of the pivot
    pivot = median_of_medians(n[start:end])
    pivot_pos = partition(n, start, end, pivot)

    # We found the kth-smallest element
    if k == pivot_pos:
        return n[pivot_pos]

    # kth-smallest element is in the left sublist (restrict end to pivot)
    if k < pivot_pos:
        return kth_mm(n, k, start, pivot_pos, root_call=False)[0] # type: ignore

    # kth-smallest element is in the right sublist (restrict start to pivot + 1)
    return kth_mm(n, k, pivot_pos + 1, end, root_call=False)[0] # type: ignore

### DRIVER METHODS
def plot(
            to_plot: list[tuple[int, float, float, float]], file_name: str
        ) -> None:
    """
    Plots a given list of selection algorithm comparison data

    Parameters
    ----------
    to_plot: list[tuple[int, float, float, float]]
        A list of tuples containing the dimensions of the list, the average
        runtime for the kth smallest element with merge-sort, quick-select,
        and quick-select with median-of-medians
    file_name: str
        The file name to save the created plot image to. Will be concatenated
        with ".png"
    """
    # Split up to_plot list
    dimensions_used = [i[0] for i in to_plot]
    kms_durations = [i[1] for i in to_plot]
    kp_durations = [i[2] for i in to_plot]
    kmm_durations = [i[3] for i in to_plot]

    # Titles and labels
    plt.title("Selection Algorithm Comparison")
    plt.xlabel("Array Length")
    plt.ylabel("Time Taken (s)")

    # Plots for each algorithm
    plt.plot(
        dimensions_used, kms_durations, color="red",
        label="Merge-Sort"
    )
    plt.plot(
        dimensions_used, kp_durations, color="green",
        label="QuickSelect"
    )
    plt.plot(
        dimensions_used, kmm_durations, color="blue",
        label="QuickSelect (w/Median of Medians)"
    )
    plt.legend()

    # Save and display
    plt.savefig(f"{file_name}.png")
    plt.show()

def execute(
            to_plot: list[tuple[int, float, float, float]] = []
        ) -> None:
    """
    Drives execution of the comparison of the algorithms.

    Parameters
    ----------
    to_plot: list[tuple[int, float, float, float]] = []
        A list of tuples containing the dimensions of the list, the average
        runtime for the kth smallest element with merge-sort, quick-select,
        and quick-select with median-of-medians. If provided, no comparisons
        will be made. Instead, the input list will be plotted using the `plot`
        function.
    """

    # Greet my super cool graders
    print("hello :)")

    # "Constants" - dimensions actually changes every iteration... but whatever
    FILE_NAME = "comparison"
    DIMENSIONS = 100
    R = 10

    # If given a list of items to plot, just plot it. No need to re-compare
    if to_plot:
        plot(to_plot, FILE_NAME)
        return

    # Gameplay loop
    while True:
        try:
            # Create the random input array and a random index to select from
            print(f"List with dimension {DIMENSIONS:_} is being created!")
            n, k = random_list_k(0, DIMENSIONS, DIMENSIONS)
            print(f"Beginning selection.")

            # Call each function 10 times for an average
            kms_average: float = 0
            kp_average: float = 0
            kmm_average: float = 0
            for _ in range(R):
                kms, kms_duration = kth_merge_sort([i for i in n], k) # type: ignore
                kms_average += kms_duration

                kp, kp_duration = kth_partition([i for i in n], k) # type: ignore
                kp_average += kp_duration

                kmm, kmm_duration = kth_mm([i for i in n], k) # type: ignore
                kmm_average += kmm_duration

                # Ensure we got the right answer
                assert selection_equality(kms, kp, kmm)
                print("All three algorithms found the same element!\n\n")

        # If something goes wrong, let's plot what we had
        except:
            break

        # Store the plotting data
        to_plot.append(
            (DIMENSIONS, kms_average/R, kp_average/R, kmm_average/R)
        )
        print(
            to_plot,
            file=open(f"{FILE_NAME}.txt", "w", encoding="utf-8")
        )

        # So many dimensions
        DIMENSIONS *= 10

    # Plotting time
    plot(to_plot, FILE_NAME)

if __name__ == "__main__":
    execute([(100, 0.0, 0.0, 9.999275207519531e-05), (500, 0.0004999637603759766, 0.00019993782043457032, 0.000700068473815918), (1000, 0.0008943080902099609, 0.00014681816101074218, 0.000851297378540039), (5000, 0.005138969421386719, 0.0005005598068237305, 0.004845857620239258), (10000, 0.011581492424011231, 0.0014954328536987305, 0.009713506698608399), (50000, 0.06869542598724365, 0.00839982032775879, 0.056070470809936525), (100000, 0.174629807472229, 0.008880877494812011, 0.11173441410064697), (500000, 0.7934062004089355, 0.09242963790893555, 0.49038770198822024), (1000000, 1.9756410121917725, 0.13993983268737792, 1.221646285057068), (5000000, 11.60554506778717, 0.6120541095733643, 7.445390796661377), (10000000, 27.11725652217865, 1.2761962175369264, 16.957574558258056), (50000000, 157.15855567455293, 6.010883235931397, 103.9824272632599), (100000000, 350.12648422718047, 10.97463779449463, 226.94087131023406)])


