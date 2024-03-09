def triangle(n):
    i,j,k=0,0,0
    for i in range(0,n): 
        print()    # to print next line
        for j in range(i+1,n): # to print the spaces in reverse
            print("-",end="")
        for k in range(j,n+i): # logic to print the star in pattern
            print("*",end="")    

n=5
triangle(n)  