L = int(input())
A = list(map(int, input().split(' ')))

if len(A) == L:
    if len(A) == len(set(A)):
        print("YES")
    else:
        print("NO")




