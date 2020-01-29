count=1
while(count>0):
  source=int(input("enter the source:"))
  dest=int(input("enter the dest:"))
  km=dest-source
  print(km)
  mini=1
  maxi=2
  prime=3
  n=int(input("choose the car:"))
  if(n==1):
    a=10
    b=10*km
    print("the amount is:",b)
  elif(n==2):
    a=20
    b=20*km
    print("the amount is:",b)
  elif(n==3):
    a=100
    b=100*km
    print("the amount is:",b)
  else:
    print("invalid choice")
  d=input("do u want to continue:")
  if(d=="yes"):
    count=1
    continue
  else:
    count=0
    break 

