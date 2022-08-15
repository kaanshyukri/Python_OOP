class dictionary_iter:

    def __init__(self, data: dict):
        self.data = (x for x in data.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
