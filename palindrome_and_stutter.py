def is_palindrome(text):
    text2=""
    text=text.lower()
    print(text)
    for i in range(len(text)-1,-1,-1):
        text2 = text2 + text[i]
    print(text2)
    if(text==text2):
        return True
    else:
        return False

variable= str("hello")
print(is_palindrome(variable))


def stutter(text):
    text2=""
    text=text.lower()
    print(text)
    for i in range(0,len(text)):
        text2 = text2 + text[i] + text[i]
    print(text2)
    
    
variable= str("hello")
print(stutter(variable))    