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


