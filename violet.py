import math


# Define a function to simulate the movement of the purple violets.
def the_purple_violets(N, M, P, commands):
    # Assert that N and M are within the specified range.
    assert 1 <= N <= 10**6, "N is out of range"
    assert 1 <= M <= 10**6, "M is out of range"
    # Assert that all elements of P are within the specified range.
    assert all(0 <= Pi <= 10**6 for Pi in P), "Some Pi is out of range"

    # Initialize the current position to the middle of the array.
    current_pos = math.ceil(N / 2) - 1

    # Iterate over the commands.
    for command in commands:
        # If the command is "r", move to the right.
        if command.lower() == "r":
            # Calculate the number of steps to move.
            steps = math.ceil((N - current_pos - 1) / 2.0)
            # Update the current position.
            current_pos += steps
        # If the command is "l", move to the left.
        elif command.lower() == "l":
            # Calculate the number of steps to move.
            steps = math.ceil(current_pos / 2.0)
            # Update the current position.
            current_pos -= steps

    # Return the value at the current position in P.
    return P[current_pos]


# Read the number of violets and the number of commands from the input.
N, M = map(int, input().split())
# Read the array of violets from the input.
P = list(map(int, input().split()))
# Read the commands from the input.
commands = input()
# Print the number of violets.
print(N)
# Print the value at the final position after executing the commands.
print(the_purple_violets(N, M, P, commands))
