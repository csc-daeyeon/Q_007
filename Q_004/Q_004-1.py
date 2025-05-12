N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = []



if len(A) <= N & len(B) >= N:
    for i in range(N):
        result.append(A[i]-B[i])
else:
    print("No")

print(*result)
