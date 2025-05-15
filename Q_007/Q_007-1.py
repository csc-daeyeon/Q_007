# N : 사용자 입력 값 
# X : 버그 입력 값 
# 입력값안에 버그의 원인이 되는 입력값 갯수 출력 

A = []
cnt = 0

N, X = map(int, input().split())

X_str = str(X)

A = list(map(str, input().split()))

for i in A:
    if X_str in i:
        cnt += 1

for i in A:
    print(i)

print(cnt)



