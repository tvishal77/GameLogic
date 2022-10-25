import random
import sys

n=True
ro=1
Player_points=0
System_points=0
while(n):
    print("Let's Start Round: ","%d"%+ro)
    Player=input("Enter your choice(rock,paper,scissors,enough): ")   #player selection option
    Options_possible=["rock","paper","scissors"]   #list of possible options for system
    System=random.choice(Options_possible)
    print(f"\nYou chose {Player}, system chose {System}.\n")
    if(Player == System):
        print("Round Tie No points!!")
        ro+=1
    elif(Player == "rock"):
        if(System == "scissors"):
            print("Hurry!! You won...:) in round - ")
            Player_points+=1
            ro+=1
        else:
            print("Oops!! You lose...:( in round - ")
            System_points+=1
            ro+=1
    elif(Player == "paper"):
        if(System == "rock"):
            print("Hurry!! You won...:) in round - ")
            Player_points+=1
            ro+=1
        else:
            print("Oops!! You lose...:( in round - ")
            System_points+=1
    elif(Player == "scissors"):
        if(System == "paper"):
            print("Hurry!! You won...:) in round - ")
            Player_points+=1
            ro+=1
        else:
            print("Oops!! You lose...:( in round - ")
            System_points+=1
            ro+=1
    elif(Player == "enough"):
        flag=False
        break
    else:
        print("Enter proper choice: ")
       
print("Total points after the tournament is")
print(f"Your points are {Player_points}")
print(f"system points are {System_points}")
if(Player_points>System_points):
    print("Congratulations!! you won the tournament...:)")
elif(Player_points<System_points):
    print("Better Luck Next Time...:(")
else:
    print("Tournament Draw...!!")

flag=True
if(flag!=True):
    sys.exit()
