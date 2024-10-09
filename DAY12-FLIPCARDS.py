T = int(input())

for _ in range(T):
    
    N, X = map(int, input().split())
    
    result = min(X, N - X)
    
    print(result)
