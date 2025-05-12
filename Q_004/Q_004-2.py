N  = list(map(int,input().split()))
student = int(N[1])
answer = []
result = []
avg = 0

for i in range(student):
    L = list(map(int, input().split()))
    answer.append(L)

for j in range(len(answer)):
    avg = sum(answer[j]) // len(answer[j])
    result.append(avg)

print(max(result))





