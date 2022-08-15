class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTest(TestCase):

    def test_cat_name(self):
        cat = Cat("Zendaya")
        self.assertEqual(cat.name, "Zendaya")

    def test_size_after_eating(self):
        cat = Cat("Zendaya")
        self.assertEqual(cat.size, 0)
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_is_fed_after_eating(self):
        cat = Cat("Zendaya")
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

    def test_if_raises_error_after_is_fed(self):
        cat = Cat("Zendaya")
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_if_raises_error_when_not_sleep(self):
        cat = Cat("Zendaya")

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        cat = Cat("Zendaya")
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)

if __name__ == "__main__":
    main()
