def quickSort(a, l, r):
    """
    Performs the QuickSort algorithm on an array.

    Args:
        a (list): The array to be sorted.
        l (int): The starting index of the subarray to be sorted.
        r (int): The ending index of the subarray to be sorted.

    Returns:
        None: The array is sorted in place.
    """
    if l < r:
        # Partition the array and get the pivot index
        q = partition(a, l, r)
        # Recursively sort the elements before the pivot
        quickSort(a, l, q - 1)
        # Recursively sort the elements after the pivot
        quickSort(a, q + 1, r)

def partition(a, l, r):
    """
    Partitions the array around a pivot such that elements less than
    or equal to the pivot are on the left, and elements greater than
    the pivot are on the right.

    Args:
        a (list): The array to be partitioned.
        l (int): The starting index of the subarray.
        r (int): The ending index of the subarray (pivot).

    Returns:
        int: The index of the pivot element after partitioning.
    """
    pivot = a[r]  # Choose the rightmost element as the pivot
    for j in range(l, r):  # Iterate over the subarray
        if a[j] <= pivot:  # If current element is less than or equal to the pivot
            a[l], a[j] = a[j], a[l]  # Swap elements to the left
            l += 1  # Increment the left boundary

    # Swap the pivot element with the element at the partition index
    a[l], a[r] = a[r], a[l]  
    return l  # Return the pivot index

# Example usage:
elements = [2, 3, 5, 3, 1, 5, 6, 4, 2, 6, 4, 3, 25, 6]
quickSort(elements, 0, len(elements) - 1)
print(elements)  # Output the sorted array
