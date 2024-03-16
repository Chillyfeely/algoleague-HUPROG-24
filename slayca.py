# Define a function that calculates the maximum number of cities that can be visited within a given budget.
def the_perfect_society(N, M, A):
    # Initialize the left pointer, total cost, and maximum number of cities that can be visited.
    left = 0
    total = 0
    max_cities = 0

    # Iterate over the cities.
    for right in range(N):
        # Add the cost to visit the current city to the total cost.
        total += A[right]
        # While the total cost exceeds the budget, move the left pointer to the right and subtract the cost to visit the leftmost city from the total cost.
        while total > M:
            total -= A[left]
            left += 1
        # Update the maximum number of cities that can be visited.
        max_cities = max(max_cities, right - left + 1)

    # Return the maximum number of cities that can be visited.
    return max_cities


# Read the number of cities and the total budget from the input.
N, M = map(int, input().split())
# Read the cost to visit each city from the input.
A = list(map(int, input().split()))
# Print the maximum number of cities that can be visited.
print(the_perfect_society(N, M, A))
