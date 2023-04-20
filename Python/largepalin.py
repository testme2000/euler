
firstseries = [i for i in range(100,1000)]
secondseries = [i for i in range(100,1000)]
palinseries = []

for numb in firstseries:
    for secondnum in secondseries:
        product = numb * secondnum
        instr = str(product)
        revstr = instr[::-1]
        if (instr == revstr):
            palinseries.append(product)
                  
largepalin = max(palinseries)
print(largepalin)