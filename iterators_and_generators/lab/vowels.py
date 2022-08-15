class vowels:

    def __init__(self, string):
        self.string = string
        self.string_len = len(string) - 1
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.string_len:
            current_string = self.string[self.i]
            self.i += 1
            if current_string in "AEIUYOaeiuyo":
                return current_string
        else:
            raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
