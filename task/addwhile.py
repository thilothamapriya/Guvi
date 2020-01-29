count=1
while(count>0):
  a=int(input("enter the number:"))
  b=int(input("enter the number:"))
  c=a+b
  print(c)
  d=input("do u want to continue:")
  if(d=="yes"):
    count=1
    continue
  else:
    count=0
    break 
