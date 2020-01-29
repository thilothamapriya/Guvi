count=1
while(count>0):
  player1=str(input("enter the action:"))
  player2=str(input("enter the action:"))
  if(player1=="scissor" and player2=="rock"):
    print("player 2 win")
  elif(player1=="scissor" and player2=="scissor"):
    print("two player chooses same")
  elif(player1=="rock"  and player2=="rock"):
    print("two player chooses same")
  elif(player1=="scissor" and player2=="paper"):
    print("player1 win")
  elif(player1=="rock" and player2=="scissor"):
    print("player1 win")
  elif(player1=="rock" and player2=="paper"):
    print("player1 win")
  elif(player1=="scissor" and player2=="paper"):
    print("player1 win")
  n=input("do u want to continue:")
  if(n=="yes"):
    count=1
    continue
  else:
    count=0
    break
