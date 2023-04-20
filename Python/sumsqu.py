sumlist = [i for i in range(1,101)]
squlist = [i ** 2 for i in range(1,101)]

allsum = sum(sumlist)
allsqusum = sum(squlist)
finalsqu = allsum ** 2
#print(finalsqu)
#print(allsqusum)
print(finalsqu - allsqusum)