import math

N = int(input())
cnt = 0

for n in range(1,N+1):
    if len(str(n)) % 2 == 1:
        cnt += 1

print(cnt)