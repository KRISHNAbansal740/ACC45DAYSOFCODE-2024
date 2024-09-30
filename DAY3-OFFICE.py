t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    total_hours = 4 * x + y
    print(total_hours)
