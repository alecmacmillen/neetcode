
def insertion_sort(input_list: list[int]) -> list[int]:
    """
    - Iterate through the list starting in position 2, call it "key"
    - Compare each element to the rightmost element in the sorted subarray
    - If the key value is larger than the right most element, insert it
    - If not, continue comparing until you reach the start of the subarray
    """
    n = len(input_list)
    # If list is only 1 element, it is already sorted
    if n <= 1:
        return
    # Iterate through the 2nd through nth elements of the list
    for i in range(1, n):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            # Make in-place swaps between adjacent sorted subarray
            # elements until you find the first subarray element
            # larger, that's how you know the key is in the right 
            # place - break the loop and stop there
            input_list[j + 1] = input_list[j]
            j -= 1
        # Insert the key one position to the right of the final
        # j-index searched by the loop (the j index represents
        # the first sorted subarray element smaller than the key)
        input_list[j + 1] = key


if __name__ == "__main__":
    l1 = [4, 3, 2, 1]
    insertion_sort(l1)
    print(l1)