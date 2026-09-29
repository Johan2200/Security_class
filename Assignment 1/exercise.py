
# public parameters:
p = 29837
g = 42
pk = 22690 #Public key

# c1 and c2 has been itercepted:
c1 = 23447
c2 = 8372

# find exponent x
for i in range(p-1):
    if pow(g, i, p) == pk:
        print(i)
        x = i
        break
        
# find m
c1_ = pow(c1,-x,p) # -x is inverse

m = c2*c1_ # Modular division means multiplying by an inverse

print(m) #prints 182174720