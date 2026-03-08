n = int(input("Enter a number: "))
def fib_seq(n):
    if n <=1:
        return n
    grandparent = 0
    parent = 1
    for i in range(n-1):
        current = parent+grandparent
        grandparent = parent
        parent = current

    return current


print("fib_seq:",fib_seq(n))