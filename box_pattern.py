def triangle(number1,number2):
    i,j=0,0
    for i in range(1,number2+1): #logic to print rows
        for j in range(1,number1+1): # logic to print columns
            if (i == 1 or i == number2 or j == 1 or j == number1) : # condition to print the spaces inside stars
                print("*",end="")
            else:    
                print(" ",end="")               
        print()
    print(max([[1, 2], [3, 4]][1]))

    print(sum([ [1, 2], [1, 1] ][0], [ [1, 2], [1, 1] ][1]))

    print(min[ [3, 2], [1, 1] ][1], [ [3, 2], [1, 1] ][1])

    print(len([ [1, 2], [3, 4], 5]))
n2=5
n1=8




triangle(n1,n2)