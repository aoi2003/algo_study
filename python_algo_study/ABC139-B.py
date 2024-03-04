A,B = map(int,(input().split()))
counter = 1
num = 0

while counter < B:
  counter = counter - 1
  counter = counter + A
  num = num + 1

print(num)