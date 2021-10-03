def fibonacci_iter(n):
    fib = [0, 1]

    i = 1
    while i < n:
        fib.append(fib[i] + fib[i - 1])
        i += 1

    return fib


def fibonacci_recursive(n, i=1, fib=[0, 1]):
    if i >= n:
        return fib
    if i < n:
        fib.append(fib[i] + fib[i - 1])
        i += 1
        return fibonacci_recursive(n, i, fib)

print(f'Ciąg fibonacciego iteracyjnie: {fibonacci_iter(6)}') # [0, 1, 1, 2, 3, 5, 8]
print(f'Ciąg fibonacciego rekurencyjnie: {fibonacci_recursive(6)}') # [0, 1, 1, 2, 3, 5, 8]