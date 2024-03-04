N,S,K = map(int, input().split())
sum = 0
for i in range(N):
  price,num = map(int, input().split())
  sum = sum + price * num

if sum >= S:
  print(sum)
else:
  sum = sum + K
  print(sum)