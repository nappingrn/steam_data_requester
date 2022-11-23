import math

def N_Pick_K(n,k): # n! / (k! * (n-k)!)

    if n == 0 or k == 0:
        return 0
    
    minus = n-k

    n = math.factorial(n)
    k = math.factorial(k)
    
    return n / (k * math.factorial(minus))

 
def Binomial_Distribution(k,n,p): # testing a push

    n_picked = N_Pick_K(n,k)

    p_to_k = p**k

    inverse_p_to_k = (1-p)**(n-k)

    total = n_picked * p_to_k * inverse_p_to_k

    return total

    
    