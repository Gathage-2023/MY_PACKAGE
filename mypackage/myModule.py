def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object 
        n (int): number of items to return
 
    Returns:
        array: top n items in descending order 

    Examples:
    >>> top_n([8,3,2,7,4], 3)
    [8, 7, 4]
    """
    for i in range(n):  # Keep sorting until we have top n items
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                # Swap the two items
                items[j], items[j + 1] = items[j + 1], items[j]

    # Get last n items
    top_n = items[-n:]

    # Return in descending order
    return top_n[::-1]

# Example usage
print(top_n([8, 3, 2, 7, 4], 3))  # Output: [8, 7, 4]

 





