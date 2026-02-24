def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Input list
nums = [2, 3, 5, 7]

# Check if all numbers are prime
all_prime = True
for x in nums:
    if isPrime(x) == False:
        all_prime = False
        break

print(all_prime)