def cache(func):

    memo = {}

    def decorator(num):
        if num in memo:
            return memo[num]
        result = func(num)
        memo[num] = result
        return result
    decorator.log = memo
    return decorator


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)
