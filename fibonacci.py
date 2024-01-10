class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        if n == 0 or n == 1:
            return n
        
        res = 0
        for i in range(n-1):
            res = f0 + f1
            f0 = f1
            f1 = res
        return res

def fib(n: int) -> int:
    f0 = 0
    f1 = 1
    arrF = []

    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    arrF = [0, 1]
    for i in range(2, n):
        res = f0 + f1
        f0 = f1
        f1 = res
        arrF.append(res)

    return arrF

print("Fibonacci series:", fib(10))