a = int(input('enter a number: '))
b= 2
while a>0:
         if b == 2 :
             print(b,end=' ')
             b += 1
             a-=1
         else:
             while True :
                 for i in range(2,b):
                     if b % i == 0:
                         b +=1
                         break
                 else:
                    print(b,end=' ')
                    b += 1
                    a -=1
                    break


