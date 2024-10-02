def fib(flist):
    nex = flist[-2]+flist[-1]
    if nex > 4000000:
        return flist
    else:
        flist.append(nex)
        return fib(flist)

fibList = fib([1,2])

tot = 0
for f in fibList:
    if f%2 == 0:
        tot += f
        print(f)

print(tot)
