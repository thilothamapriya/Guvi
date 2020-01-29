b=int(input("enter the number:"))
c=int(input("enter the number:"))
sum=0
for i in range(b,c):
  if(i%2 != 0):
    a=i
    i=sum+i
    sum=i
print("The sum of odd numbers:",sum)
  
