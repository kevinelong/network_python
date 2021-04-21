def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)  # RECURSE


last = 0
for i in range(10):
    number = fib(i)
    if last > 0:
        print(number, last / number)  # FI THE GOLDEN RATIO APPROXIMATED
    last = number
