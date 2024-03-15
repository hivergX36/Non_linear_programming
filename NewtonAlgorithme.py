f = lambda x: 2*x**2 
f_prime = lambda x: 4*x

#On peut améliorer le pas

def descent_gradient(f,f_prime,x_0,number_iteration):
    x = 10
    print(x)
    for i in range(number_iteration):
        print(i)
        x = x - 0.1*f_prime(x)
        print(x)
    return x



y = descent_gradient(f,f_prime, 20, 10000)
print(y)