from collections import defaultdict
from math import factorial


# Define a recursive function to find all paths from start to end with a maximum length of 3.
def dfs(graph, start, end, path, all_paths):
    path = path + [start]
    # If the start node is the end node and the path length is 3, add the path to all_paths.
    if start == end and len(path) == 3:
        all_paths.add(tuple(path))
    # If the path length is less than 3, continue to explore the graph.
    elif len(path) < 3:  # Limit path length to 3 (including start and end)
        for node in graph[start]:
            # Avoid cycles by checking if the node is already in the path.
            if node not in path:
                dfs(graph, node, end, path, all_paths)


# Define a function to find all valid paths in the graph.
def find_threesome_paths(graph, n):
    valid_paths = defaultdict(set)
    # Iterate over all pairs of nodes.
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            # Avoid paths from a node to itself.
            if start != end:
                all_paths = set()
                # Find all paths from start to end.
                dfs(graph, start, end, [], all_paths)
                # If there are any paths, add them to valid_paths.
                if all_paths:
                    valid_paths[(start, end)].update(all_paths)
    return valid_paths


# Define a function to calculate the binomial coefficient.
def binomial_coefficient(n, k):
    if n < k:
        return 0
    # Use the formula n! / (k!(n-k)!)
    return factorial(n) // (factorial(k) * factorial(n - k))


# Define a function to read the input and find all valid paths.
def main():
    first_line = input().split()
    n, m, k = int(first_line[0]), int(first_line[1]), int(first_line[2])
    graph = defaultdict(list)

    # Read the edges of the graph.
    for _ in range(m):
        edge = input().split()
        a, b = int(edge[0]), int(edge[1])
        graph[a].append(b)

    # Find all valid paths.
    valid_paths = find_threesome_paths(graph, n)
    sum_of_ways = 0

    # Calculate the sum of the binomial coefficients of the lengths of the valid paths.
    for _, paths in valid_paths.items():
        ways = binomial_coefficient(len(paths), k)
        sum_of_ways += ways

    # Print the sum of the binomial coefficients.
    print(sum_of_ways)


if __name__ == "__main__":
    main()
