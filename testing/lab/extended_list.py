class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_data_with_no_integers(self):
        integer = IntegerList("abv", 10.5)
        self.assertEqual(integer._IntegerList__data, [])

    def test_data_with_integers(self):
        integer = IntegerList(1, 2, 3, 5)
        self.assertEqual(integer._IntegerList__data, [1, 2, 3, 5])

    def test_get_data(self):
        integer = IntegerList(1, 2, 3, 5)
        self.assertEqual(integer.get_data(), [1, 2, 3, 5])

    def test_add_raises_error_string(self):
        integer = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ex:
            integer.add("5")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_add_with_integer(self):
        integer = IntegerList(1, 2, 3)
        self.assertEqual(integer.add(5), [1, 2, 3, 5])

    def test_remove_index_with_no_such_index(self):
        integer = IntegerList(1, 2)
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_remove_index_in_range(self):
        integer = IntegerList(1, 2)
        self.assertEqual(integer.remove_index(0), 1)

    def test_get_with_index_more_than_len(self):
        integer = IntegerList(1, 5, 4)
        with self.assertRaises(IndexError) as ex:
            integer.get(5)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_with_index_in_range(self):
        integer = IntegerList(1, 3, 4)
        self.assertEqual(integer.get(2), 4)

    def test_insert_with_index_not_in_range(self):
        integer = IntegerList(1, 5, 4)
        with self.assertRaises(IndexError) as ex:
            integer.insert(5, 2)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_index_then_get_data(self):
        integer = IntegerList(0, 2, 3)
        integer.insert(1, 1)
        self.assertEqual(integer.get_data(), [0, 1, 2, 3])

    def test_insert_with_element_string(self):
        integer = IntegerList(1, 5, 4)
        with self.assertRaises(ValueError) as ex:
            integer.insert(5, "5")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_get_biggest(self):
        integer = IntegerList(-2, -5, 20, 100, 15, 1, 78, 6)
        self.assertEqual(integer.get_biggest(), 100)

    def test_get_index(self):
        integer = IntegerList(-2, -1, 0, 1, 2, 3)
        self.assertEqual(integer.get_index(0), 2)


if __name__ == "__main__":
    main()