"""AtCoder Beginner Contest 322 A"""
n = int(input())
s = input()

result = -1
for i in range(n - 2):
    if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
        result = i + 1
        break

print(result)