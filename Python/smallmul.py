allmult = []
alldiv = [i for i in range(1,21)]


for num in range(232792561):
    for divnum in alldiv:
        if num % divnum != 0:
            break
        if divnum == 20:
            allmult.append(num)
print(allmult)