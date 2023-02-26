b = int(input(),16)
i=1
while True:
    mul = b*i
    print("%X"%b,"*","%X"%i,"=","%X"%mul,sep="")
    
    i += 1
    if i==16:
        break