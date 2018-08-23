from Q1 import primenumber

def largest_prime_number(x):
    list_of_primes=[]
    for i in range(2,x):
        if primenumber(i)==True:
            list_of_primes.append(i)
            print (i)
    return list_of_primes

print(largest_prime_number(100))





