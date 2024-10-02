T = int(input())

for _ in range(T):
    B1, B2, B3 = map(int, input().split())

    empty_count = (B1 == 0) + (B2 == 0) + (B3 == 0)
    
    if empty_count >= 2:
        print("Water filling time")
    else:
        print("Not now")
