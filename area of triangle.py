a = int(input('Enter first side of length: '))
b = int(input('Enter second side of length: '))
c = int(input('Enter third side of length: '))
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**(0.5)
print('Area of triangle =', area)
