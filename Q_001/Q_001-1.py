# ・Sは英小文字のみからなる文字列
# ・1 <= N <= 100
# ・1 <= i <= 100
# ・p(i)は1以上の整数

#入力例2:
#coding
#5
#1 1 2 1 3
#出力例2:
#coding a a aa a aaa

S = input()
N = int(input())
p = list(map(int, input().split(' ')))

for i in range (N):
    word = ' ' + ('a' * p(i))
    answer += word

print(answer)
    



        
