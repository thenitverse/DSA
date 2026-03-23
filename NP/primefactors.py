import math
def prime_factors(n):
    prime = []
    while n % 2 == 0:
        n = n // 2
        prime.append(2)

    for i in range(3,int(math.sqrt(n)+1)):
        while n % i == 0:
            n = n // i
            prime.append(i)

    if n > 2:
        prime.append(n)

    return prime
    
n = int(input("Enter the number: "))
print(f"prime factores of {n} = ",prime_factors(n))

