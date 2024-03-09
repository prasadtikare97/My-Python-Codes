def is_palindrome(a):
        if len(a)==0 or len(a)==1:
                return True
        reverse_list=a[::-1]
        print(reverse_list)
        if(a==reverse_list):
                return True
        else:
                return False
        
a1=["alpha", "beta", "gamma", "delta", "gamma", "beta"]
is_palindrome(a1)