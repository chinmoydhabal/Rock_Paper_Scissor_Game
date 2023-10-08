import random
def gamewin(Computer, You):
    if Computer==You:
        return None
    elif Computer=='r':
        if You =='s':
            return False
        elif You=='p':
            return True
    elif Computer=='p':
        if You=='r':
            return False
        elif You=='w':
            return False
        elif You=='s':
            return True
    elif Computer=='s':
        if You=='p':
            return False
        elif You=='r':
            return True
#print("Computer Turn: Rock(r) Paper(p) or Scissor(s)\n")
random_no=random.randint(1, 3)
if random_no==1:
    Computer='r'
elif random_no==2:
    Computer='p'
elif random_no==3:
    Computer='s' 
You=input("Your Turn: Rock(r) Paper(p) or Scissor(s): ")
a=gamewin(Computer, You)
print(f"Computer choose: {Computer}")           
print(f"You choose: {You}")

if a==None:
    print("The game is tie!")
elif a==True:
    print("You win!")
else:
    print("You lose!")
