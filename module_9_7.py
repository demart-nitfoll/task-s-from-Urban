def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result <= 1:
            print("Ни то, ни сё")
            return
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c
result_ = sum_three(2, 3, 6)
print(result_)