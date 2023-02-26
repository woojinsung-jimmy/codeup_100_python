r, g, b= input().split()
r = int(r)
g = int(g)
b = int(b)

c=0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            c+=1
print(c)

# 코드업엔 시간초과라 뜸