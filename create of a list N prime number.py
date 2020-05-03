a = int(input('Enter a number: '))
c = 2
b =[]
while a > 0:
    while True:

            for i in range(2,c):
                if c % i == 0:
                    c += 1
                    break
            else:
                b.append(c)
                c += 1
                a -= 1
                break
print(b)


