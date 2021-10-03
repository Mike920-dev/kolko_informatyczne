def collatz_iter(n):
    length = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        
        length += 1

    return length

def collatz_recursive(n, length=0):
    if n == 1:
        return length
    if n % 2 == 0:
        n /= 2
        length += 1
        return collatz_recursive(n, length)
    else:
        n = 3 * n + 1
        length += 1
        return collatz_recursive(n, length)

print(f'Collatz iteracyjnie: {collatz_iter(32)}') # 5
print(f'Collatz rekurencyjnie: {collatz_iter(32)}') # 5