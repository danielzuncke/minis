import json

try:
    prime_numbers = json.load(open('prime_numbers.json'))
except Exception as ex:
    print(ex)
    prime_numbers = [2, 3]

def grow_prime_number():
    number = prime_numbers[len(prime_numbers) - 1] + 2
    len_old = prime_numbers[len(prime_numbers) - 1]
    while len_old == prime_numbers[len(prime_numbers) - 1]:
        for x in prime_numbers:
            if number % x == 0:
                break
            if x == prime_numbers[len(prime_numbers) - 1]:
                prime_numbers.append(number)
        number += 2

def prime_factorization(number):
    while 0.5 * number > prime_numbers[len(prime_numbers) - 1]:
        grow_prime_number()
    factors =[]
    while number not in prime_numbers:
        for x in prime_numbers:
            if number % x == 0:
                factors.append(x)
                number /= x
                break
    factors.append(int(number))
    return factors

number = 0
for x in range(3):
    number = int(input('\nIn: '))
    if number > 1:
        break

print('Primfaktorzerlegung:', prime_factorization(number), end='\n')

# update json
try:
    old = json.load(open('prime_numbers.json'))
    if len(old) < len(prime_numbers):
        json.dump(prime_numbers, open('prime_numbers.json', 'w'))
except Exception as ex:
    print(ex)
    json.dump(prime_numbers, open('prime_numbers.json', 'w'))