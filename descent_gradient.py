f = lambda x: 2*x**2 
f_prime = lambda x: 4*x
f_second = lambda x: 4  
#On peut améliorer le pas

def descent_gradient(f,f_prime,x_0,number_iteration):
    x = f(x_0)
    print(x)
    for i in range(number_iteration):
        print(i)
        x = x - 0.3*f_prime(x)
        print(x)
    return x



y_1 = descent_gradient(f,f_prime, 20, 4)
print("y_1: ", y_1)

#Avec amélioration du pas

def descent_newton_gradient(f,f_prime,f_second,x_0,number_iteration):
    x = f(x_0)
    print(x)
    for i in range(number_iteration):
        print(i)
        x = x - 1/f_second(x) * f_prime(x)
        print(x)
    return x

y_2 = descent_newton_gradient(f,f_prime,f_second,20,1)
print("y_2: ", y_2)