def max(x,y):
    if ( x > y ): 
        return x
    else:
        return y

x = int(input('Enter first number \n'))
y = int(input('Enter second number \n'))
print('Largest Number is ', max(x,y))
