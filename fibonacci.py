# 0 1 1 2 3
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(n):
    print(fibonacci(i))
