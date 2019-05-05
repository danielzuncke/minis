n = int(input('n: '))

living = []
for i in range(n):
    living.append(i + 1)

killed = []
pos = 0
n -= 1

while len(living) > 1:
    if pos >= n:
        pos = abs(n - pos) - 1
    killed.append(living[pos + 1])
    living.pop(pos + 1)
    pos += 1
    n -= 1

print('alive:', living, end='\n')
print('killed (in order first to last):', killed, end='\n\n')