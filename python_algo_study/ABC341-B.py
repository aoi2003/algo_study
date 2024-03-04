N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
    s, t = map(int, input().split())
    x = A[i] // s
    A[i] -= s * x
    A[i + 1] += t * x

print(A[-1])
