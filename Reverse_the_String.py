def print_number_square(min,max):
    first_string =""   #assigning empty string
    for i in range(min,max+1):
        first_string=first_string + str(i) #storing the numbers in string

    for i in range(min,max+1):
        print(first_string) # print the numbers
        #logic to take the first number from string from add at last
        first_number=(str(first_string)[0]) 
        first_string=first_string[1:] 
        first_string+= first_number
    

min=1
max=5
print_number_square(min,max)