import heapq


def max_peaches(N, D, A):
    assert 1 <= N <= 10**5, "N is out of range"
    assert all(0 <= Di <= 10**4 for Di in D), "Some Di is out of range"
    assert all(0 <= Ai <= 10**4 for Ai in A), "Some Ai is out of range"
    heap = []  # Heap to keep track of peaches and their expiry dates.
    total_peaches_eaten = 0
    day = 0  # Initialize the day counter.

    # Calculate the maximum possible day to consider, in case we need to go beyond the provided arrays.
    # This is to ensure we process days until all peaches have been considered for consumption.
    max_days = len(D) + max(A)

    while day < max_days:
        # Add new peaches for the current day to the heap, if there are any.
        if day < len(D) and D[day] > 0:
            heapq.heappush(heap, (day + A[day], D[day]))

        # Eat a peach if there's any that hasn't expired.
        while heap:
            nearest_expiry, available_peaches = heapq.heappop(heap)
            if nearest_expiry > day:  # Check if the peach hasn't expired.
                total_peaches_eaten += 1
                if available_peaches > 1:
                    # If there are more peaches that haven't been eaten, put them back with one less.
                    heapq.heappush(heap, (nearest_expiry, available_peaches - 1))
                break  # Stop after eating one peach for the day.

        day += 1  # Move to the next day.

    return total_peaches_eaten


# Input processing
N = int(input())
D = list(map(int, input().split()))
A = list(map(int, input().split()))

# Calculate and output the maximum number of peaches Bahattin can eat
print(max_peaches(N, A, D))
