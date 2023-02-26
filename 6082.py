n = str(input())
a = 1


for i in range(int(n)):
    for j in range(len(str(a))):
        if str(a)[j] == '3' or str(a)[j] == '6' or str(a)[j] == '9':
            print('X',end='')
        else:
            print(str(a)[j],end='')
    print(' ',end='')
    a += 1