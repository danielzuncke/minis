n = 100

for x in range(1, n):
    y = ""

    if x % 3 == 0:
        y += "foo"
    if x % 7 == 0:
        y += "bar"
    if len(y) == 0:
        y += str(x)
    
    print(y)