def squares(num):
    for i in range(1, num + 1):
        yield i * i

print(list(squares(5)))