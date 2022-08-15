from unittest import TestCase, main

from examp_prep.apr import Mammal


class MammalTest(TestCase):

    def test_init_return_proper(self):
        mammal = Mammal("Ivan", "Dog", "Woff")
        self.assertEqual(mammal.name, "Ivan")
        self.assertEqual(mammal.type, "Dog")
        self.assertEqual(mammal.sound, "Woff")
        self.assertEqual(mammal._Mammal__kingdom, "animals")

    def test_make_sound_return_proper(self):
        mammal = Mammal("Ivan", "Dog", "Woff")
        result = mammal.make_sound()
        expected = f"{mammal.name} makes {mammal.sound}"
        self.assertEqual(expected, result)

    def test_get_kingdom_return_proper(self):
        mammal = Mammal("Ivan", "Dog", "Woff")
        result = mammal.get_kingdom()
        expected = mammal._Mammal__kingdom
        self.assertEqual(expected, result)

    def test_info_return_proper(self):
        mammal = Mammal("Ivan", "Dog", "Woff")
        result = mammal.info()
        expected = f"{mammal.name} is of type {mammal.type}"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()