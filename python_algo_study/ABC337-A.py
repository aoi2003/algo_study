N = int(input())
Xs = []
Ys = []

for i in range(N):
  X,Y = map(int,input().split())
  Xs.append(X)
  Ys.append(Y)

if sum(Xs) == sum(Ys):
  print("Draw")
elif sum(Xs) >= sum(Ys):
  print("Takahashi")
else:
  print("Aoki")
