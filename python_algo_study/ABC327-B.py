B = int(input())
result = -1
for i in range(1,16):
  for j in range(1,16):
    if i**j == B and i==j:
      result = i
      break

print (result)