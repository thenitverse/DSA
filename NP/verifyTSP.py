def verify_tsp(paths, dist, actual_path):
    total = 0

    for i in range(1, len(actual_path)):
        total += paths[actual_path[i - 1]][actual_path[i]]

    return total < dist


print(verify_tsp([[0, 394], [394, 0]], 3458, [0, 1]))   # True
print(verify_tsp([[0, 10, 1], [10, 0, 1], [1, 1, 0]], 9, [0, 2, 1]))  # True
print(verify_tsp([[0, 1, 1], [1, 0, 100], [1, 100, 0]], 50, [1, 2]))  # False