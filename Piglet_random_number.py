import random

def is_Piglet():
   number=0
   
   print("Welcome to Piglet!")
   choice ='yes'
   while(choice=='yes' or choice=='y'):
    roll=random.randint(1,6)
    print("You rolled a ",+roll)
    if(roll == 1):
      print("You got 0 points.")
      return
    else:
        number=number+roll;    
    print("Roll again?",end="")
    choice=str(input())
   print("You got ",number," points.") 

is_Piglet()