def max_of_three( x , y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

x = int(input('Enter first number \n'))
y = int(input('Enter second number \n'))
z = int(input('Enter third number \n'))
print('Largest Number is ', max_of_three(x,y,z))