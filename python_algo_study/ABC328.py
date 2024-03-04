n = int(input())
x = int(input())
s = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    if s[i] <= x:
        ans += s[i]

print(ans)
