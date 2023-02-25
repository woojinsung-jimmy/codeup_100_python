a = int(input())
if a==12 or a==1 or a==2:
    print('winter')
else:
    if a//3 == 1:
        print('spring')
    else:
        if 6<=a<=8:
            print('summer')
        else:
            print('fall')