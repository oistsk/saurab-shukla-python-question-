a = 1
while a <10000:
    c = 0
    b = str(a)
    j = len(b)
    for i in b:
        c = c + (int(i) ** j)
    if a == c:
        print(a)
    a += 1
