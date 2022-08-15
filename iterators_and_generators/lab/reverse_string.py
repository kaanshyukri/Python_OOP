def reverse_text(string):
    string = list(reversed(string))
    for i in range(len(string)):
        yield string[i]


for char in reverse_text("step"):
    print(char, end='')
