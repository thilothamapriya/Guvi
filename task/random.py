import random
def rand():
    r=random.randint(0,1000)
    return r
r=rand
a=int(input("enter the number:"))
print(a)
if(a==r):
  print("sucess")
else:
  print("not match")

