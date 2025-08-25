import random
''' 
1 for snake 
-1 for water
0 for gun
'''

computer= random.choice([-1,0,1])
yourstr = input("enter your choice")
yourdict = {"s":1, "w":-1,"g":0}
reversedict = {1:"snake", -1:"water",0:"gun"}

you = yourdict[yourstr]
print(f"you chose{reversedict[you]}\n computer chosee{reversedict[computer]}")
if(computer==you):
    print("its draw")
else:
    if(computer==-1 or you ==1):
        print("you win")
    elif(computer==-1 or you ==0):
        print("you lose")
    elif(computer==1 or you==-1):
        print("you lose")
    elif(computer==1 or you ==0):
        print("you win ")
    elif(computer ==0 or you ==-1):
        print("you win")
    elif(computer == 0 or you ==1):
        print("you lose")
    else:
        print("something went wrong")
        