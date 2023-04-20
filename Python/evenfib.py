
start = 1
previous = start
current = start

def generatefib(previous,current):
    return previous + current

alleven = 0
while current < 4000000:
    result = generatefib(previous,current)
    if result % 2 == 0:
        print("found even ",result)
        alleven += result
    previous = current
    current = result
    print(previous,current)

print("allevent",alleven)



