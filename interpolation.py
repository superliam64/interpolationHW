
f(x) = 1/(25*x**2+1)

A=matrix(QQ,11,11)
for i in range(11):
    for j in range(11):
        A[i,j]=n((i*.2-1.0)**j)

v=vector(QQ,11)
for i in range(11):
    v[i]=f(i)

def p(x):
    sum=0
    w=A\v
    for i in range(11):
        sum = sum + w[i]*x**i
    return sum

plot(p)