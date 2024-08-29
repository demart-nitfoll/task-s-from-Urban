numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
print(f'numbers = {numbers}')
for i in range(len(numbers)):
    is_prime = True
    if numbers[i] <= 1:
        is_prime = False
        continue
    elif numbers[i] == 2:
        is_prime = True
    else:
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
    if numbers[i] == 1:
        continue
    elif is_prime == False:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
