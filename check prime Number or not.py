a = int(input('Enter a prime number: '))
if a == 2 :
    print('it is a prime number')
elif a == 0 or a == 1 or a<0:
    print('Please Enter Valid Number.')
else:
    for i in range(2,a):
        if a % i == 0:
            print('It is not a prime number: ')
            break
    else:
            print('It is a prime number.')