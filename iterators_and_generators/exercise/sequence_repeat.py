class sequence_repeat:

    def __init__(self, string, num):
        self.string = string
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == 0:
            raise StopIteration
        current = self.string[self.count]
        self.num -= 1
        self.count += 1
        if self.count > len(self.string) - 1:
            self.count = 0
        return current


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
