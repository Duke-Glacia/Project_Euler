def prime(x):
    a=[]
    for i in range(2,x):
        if x%i==0:
            a.append(i)
    if len(a)==0:
        return True

def nth_prime_number(n):
    list_of_primes=[]
    p=0
    while len(list_of_primes)<=n:
        p+=1
        if prime(p)==True:
            list_of_primes.append(p)
    return(list_of_primes[-1])

print(nth_prime_number(10001))