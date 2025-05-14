# N : 집단 수 
# X : 점수 
# 각 집단의 최대 값을 제거 -> 각 집단의 최소 값을 제거 = 이 작업을 N번 시행 

N = int(input())
point = []
result = 0

point=sorted((list(map(int, input().split()))))

for _ in range(N):
    point.remove(max(point))
    point.remove(min(point))

result = sum(point) / len(point)

print(result)


