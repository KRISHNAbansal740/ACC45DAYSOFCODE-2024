def max_points(t, test_cases):
    results = []
    for x, y in test_cases:
    
        points_a_first = max(0, 500 - 2 * x) + max(0, 1000 - 4 * (x + y))
    
        points_b_first = max(0, 1000 - 4 * y) + max(0, 500 - 2 * (x + y))
        
        results.append(max(points_a_first, points_b_first))
    return results


t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = max_points(t, test_cases)

for res in results:
    print(res)
