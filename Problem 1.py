mults = []
for i in range(0,1000,3):
    mults.append(i)

for i in range(0,1000,5):
    if i not in mults:
        mults.append(i)

tot = 0
for m in mults:
    tot += m

print(tot)
