# Define a function to calculate the maximum number of balloons that can be hit.
def max_balloons_hit(N, W, H, balloons):
    # Convert the list of balloons into a set for faster lookup.
    balloon_set = set(balloons)

    # Define a nested function to simulate hitting balloons starting from a given position.
    def simulate_hit(start_x, start_y):
        # Initialize the set of hit balloons with the starting position.
        hit = set([(start_x, start_y)])
        # Initialize the list of positions to visit with the starting position.
        to_visit = [(start_x, start_y)]

        # While there are positions to visit,
        while to_visit:
            # Pop a position from the list.
            x, y = to_visit.pop()
            # For each direction,
            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                # Calculate the next position.
                nx, ny = x + dx, y + dy
                # If the next position is in the set of balloons and has not been hit yet,
                if (nx, ny) in balloon_set and (nx, ny) not in hit:
                    # Add it to the set of hit balloons.
                    hit.add((nx, ny))
                    # Add it to the list of positions to visit.
                    to_visit.append((nx, ny))

        # Return the number of hit balloons.
        return len(hit)

    # Initialize the maximum number of hits to 0.
    max_hits = 0
    # For each balloon,
    for balloon in balloons:
        # Update the maximum number of hits.
        max_hits = max(max_hits, simulate_hit(*balloon))

    # Return the maximum number of hits.
    return max_hits


# Read the number of balloons, the width, and the height from the input.
N, W, H = map(int, input().split())
# Read the positions of the balloons from the input.
balloons = [tuple(map(int, input().split())) for _ in range(N)]
# Print the maximum number of balloons that can be hit.
print(max_balloons_hit(N, W, H, balloons))
