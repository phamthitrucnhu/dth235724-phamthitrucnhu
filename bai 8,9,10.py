n=4
for i in range(n):
    row =[]
    for j in range(n):
        if i in (0,n-1) or j in (0,n-1):
            row.append('*')
        else:
            row.append(' ')
    print(''.join(row))


    def hcn(cao,rong):
        for i in range(cao):
            print ("*"*rong)

    hcn(4,9)

