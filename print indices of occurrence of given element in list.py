a = eval(input('Enter a number: '))
element = int(input('Enter a number: '))
count = 0
for i in a:
    if i == element:
        print(count,end=' ')
    count += 1
