N = int(input())
Ps = list(map(int, input().split()))
Max = max(Ps)
if Max+1 < Ps[0]:
  ans = 0
else:
  ans = (Max+1) - Ps[0]
print(ans)

"""AtCoder Beginner Contest 313 A"""
n = int(input())
p = list(map(int, input().split()))

maxp = max(p[1:]) if n > 1 else p[0] - 1
print(0 if p[0] > maxp else maxp + 1 - p[0])