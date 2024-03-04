N,P,Q = map(int,input().split()) 
D_list = list(map(int,input().split()))

if P < (Q + min(D_list)):
  print(P)
else:
  print(Q+min(D_list))