a = int(input('Enter a number: '))
product = 1
count = 1
while a>0:
    product *= count
    count +=1
    a -= 1
print(product)