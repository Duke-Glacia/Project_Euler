def primenumber(z):
    y=[]
    for i in range(2,z):
        if z%i==0:
        	y[i]=i
    if len(y)==0:
        return True
    else:
        return False

#primenumber(110)
#Note that this is a subset of the Q3. Has no connection with Q1. 


