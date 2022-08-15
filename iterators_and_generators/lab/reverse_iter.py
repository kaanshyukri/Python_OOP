class reverse_iter:

    def __init__(self, pack):
        self.pack = pack
        self.pack_length = len(pack) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.pack_length >= 0:
            current = self.pack[self.pack_length]
            self.pack_length -= 1
            return current
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
