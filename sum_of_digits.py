def sum_of_digits():
    digit1=int(input())
    result=abs(digit1)
    count=0
    
    digits=[int(number) for number in str(result)]

    for number2 in digits:
        count=count+number2   

    print(count)       
sum_of_digits()