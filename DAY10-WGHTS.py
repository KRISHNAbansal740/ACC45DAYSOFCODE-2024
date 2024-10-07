def can_measure_weight(W, X, Y, Z):

    possible_weights = {X, Y, Z, X + Y, X + Z, Y + Z, X + Y + Z}
    return "YES" if W in possible_weights else "NO"

T = int(input())
results = []

for _ in range(T):
    W, X, Y, Z = map(int, input().split())
    results.append(can_measure_weight(W, X, Y, Z))

for result in results:
    print(result)
