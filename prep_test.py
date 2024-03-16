# Define a function to find the index of the maximum value in a list.
def find_max_index(M, arr):
    # Assert that M is within the specified range.
    assert 5 <= M <= 10**6, "M is out of range"

    # Initialize the maximum value to the first element of the list.
    max_val = arr[0]
    # Iterate over the list starting from the second element.
    for i in range(1, M):
        # If the current element is less than the maximum value, return the index of the maximum value.
        if arr[i] < max_val:
            return i - 1
        # Update the maximum value.
        max_val = arr[i]

    # If all elements are in non-decreasing order, return "YES".


# Read the number of elements in the list from the input.
M = int(input().strip())
# Read the list from the input.
arr = list(map(int, input().split()))
# Print the index of the maximum value in the list.
print(find_max_index(M, arr))
