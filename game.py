'''***********************************************************************************************************************
                                welcome to rock paper Scissors game
**********************************************************************************************************************'''


import random

def gamewin(your,comp):
    if your==comp:
        return None

    if your==1:
        if comp==2:
            return False
        elif comp==3:
            return True
    
    elif your==2:
        if comp==1:
            return True
        elif comp==3:
            return False
    
    elif your==3:
        if comp==1:
            return False
        elif comp==2:
            return True


print("Comp turn:::Choose Rock(1), Paper(2) or Scissors(3):")
comp=random.randint(1,3)
your=int(input("Your turn:::Choose Rock(1), Paper(2) or Scissors(3):"))
res=gamewin(your,comp)
if res==None:
    print("The game is tied!!!!!!!!!")
elif res==True:
    print("You won the game!!! congrats")
elif res==False:
    print("You lost the game!!! Better luck next time")
