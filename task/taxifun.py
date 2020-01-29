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
  def mini():
    print("the amount per km 20")
    a=20
    b=a*km
    print("the amount is:",b)
    return b
  def macro():
    print("the amount per km is 30")
    a=30
    b=a*km
    print("the amount is",b)
    return b
  def prime():
    print("the amount per km is 100")
    a=100
    b=a*km
    print("the amount is:",b)
    return b
  if(n==1):
    mini()
  elif(n==2):
    macro()
  elif(n==3):
    prime()
  else:
    print("invalid choice")
  d=input("do u want to continue:")
  if(d=="yes"):
    count=1
    continue
  else:
    count=0
    break 
