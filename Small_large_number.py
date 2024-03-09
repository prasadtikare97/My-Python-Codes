
def smallest_largest():
    my_list=[]
 
    size=int(input("How many numbers do you want to enter? ")) # enter size
    for i in range(1,size+1):# run till size
        number =int(input(f"Number {i}: ")) #take the input from user
        my_list.append(number) # add to list
        x=3
        y=5
        point = "("+ str(x) + "," + str(y)+")"
    print( sum({1: 2, 0: 2, 2: 3}))
    smallest=my_list[0]#initialize smallest and largest number
    largest=my_list[0]
    for i in my_list:
        if i < smallest : #condition to check if the number is smallest or largest
            smallest=i
        elif i> largest:
            largest=i
    print(f"Smallest = {smallest}")#print smallest and largest
    print(f"Largest = {largest}")      
    x,r=0,0     
    for x in range(0,6):
        print()
        for r in range(6,x,-1):
            print(" ",end="")
        for r in range(0,x):
            print("*",end="")




smallest_largest()