def prime_numbers(n):
    arr_prime = []

    for i in range(2, n):
        is_prime = True

        # Check if i is divisible by any number between 2 and the square root of i
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            arr_prime.append(i)

    return arr_prime

print("Prime number series:", prime_numbers(10))
