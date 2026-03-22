def tsp(cities, paths, dist):
    path = permutations(cities)
    for p in path:
        total = 0
        for i in range(1, len(p)):
            total += paths[p[i - 1]][p[i]]
        if total < dist:
            return True
    return False


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res


# --- Test Cases ---

# 2 cities, distance 394, asking if path < 3458 → True
print(tsp([0, 1], [[0, 394], [394, 0]], 3458))  # Expected: True

# 2 cities, distance 394, asking if path < 300 → False
print(tsp([0, 1], [[0, 394], [394, 0]], 300))  # Expected: False

# 3 cities, best path is 0->2->1 = 430+41 = 471, asking < 3104 → True
print(tsp([0, 1, 2], [[0, 911, 430], [911, 0, 41], [430, 41, 0]], 3104))  # Expected: True

# 4 cities, asking < 1877 → True
print(tsp(
    [0, 1, 2, 3],
    [
        [0, 988, 523, 497],
        [988, 0, 850, 940],
        [523, 850, 0, 802],
        [497, 940, 802, 0],
    ],
    1877
))  # Expected: True

# 7 cities, tight distance → False
print(tsp(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [
        [0, 63, 824, 940, 561, 937, 14, 95],
        [63, 0, 736, 860, 408, 727, 844, 803],
        [824, 736, 0, 684, 640, 1, 626, 505],
        [940, 860, 684, 0, 847, 888, 341, 249],
        [561, 408, 640, 847, 0, 747, 333, 720],
        [937, 727, 1, 888, 747, 0, 891, 64],
        [14, 844, 626, 341, 333, 891, 0, 195],
        [95, 803, 505, 249, 720, 64, 195, 0],
    ],
    1066
))  # Expected: False