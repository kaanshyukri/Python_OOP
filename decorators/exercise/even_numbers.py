def even_parameters(func_ref):

    def decorator(*nums):

        for num in nums:
            if isinstance(num, str) or num % 2 != 0:
                return "Please use only even numbers!"
        return func_ref(*nums)
    return decorator


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
