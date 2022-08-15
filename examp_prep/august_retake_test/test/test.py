from august_retake_test.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):

    def test_init(self):
        library = Library("Shumen")
        self.assertEqual("Shumen", library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_name_raises_error_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            library = Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_author_and_title_in_books_by_authors(self):
        library = Library("Shumen")
        library.books_by_authors["Ivan"] = ["Friends", "Enemies"]
        library.add_book("Ivan", "Enemies")
        self.assertEqual({"Ivan": ["Friends", "Enemies"]}, library.books_by_authors)

    def test_add_book_only_title_not_in_dict(self):
        library = Library("Shumen")
        library.books_by_authors["Ivan"] = ["Friends", "Enemies"]
        library.add_book("Ivan", "Love")
        self.assertEqual({"Ivan": ["Friends", "Enemies", "Love"]}, library.books_by_authors)

    def test_add_book_author_and_title_not_in_dict(self):
        library = Library("Shumen")
        library.books_by_authors["Ivan"] = ["Friends", "Enemies"]
        library.add_book("Gosho", "Impact")
        expected = {"Ivan": ["Friends", "Enemies"], "Gosho": ["Impact"]}
        self.assertEqual(expected, library.books_by_authors)

    def test_add_reader_return_text_not_in_dict(self):
        library = Library("Shumen")
        library.readers["Ivan"] = []
        result = library.add_reader("Ivan")
        expected = "Ivan is already registered in the Shumen library."
        self.assertEqual(expected, result)

    def test_add_reader_not_in_dict(self):
        library = Library("Shumen")
        library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, library.readers)

    def test_rent_book_reader_not_in_readers(self):
        library = Library("Shumen")
        result = library.rent_book("Ivan", "Gosho", "Impact")
        expected = "Ivan is not registered in the Shumen Library."
        self.assertEqual(expected, result)

    def test_rent_book_author_not_in_books(self):
        library = Library("Shumen")
        library.add_reader("Ivan")
        result = library.rent_book("Ivan", "Gosho", "Impact")
        expected = "Shumen Library does not have any Gosho's books."
        self.assertEqual(expected, result)

    def test_rent_book_title_not_in_books(self):
        library = Library("Shumen")
        library.add_reader("Ivan")
        library.add_book("Gosho", "Friends")
        result = library.rent_book("Ivan", "Gosho", "Impact")
        expected = """Shumen Library does not have Gosho's "Impact"."""
        self.assertEqual(expected, result)

    def test_rent_book(self):
        library = Library("Shumen")
        library.add_reader("Ivan")
        library.add_book("Gosho", "Friends")
        library.rent_book("Ivan", "Gosho", "Friends")
        expected = {"Ivan": [{"Gosho": "Friends"}]}
        result = library.readers
        self.assertEqual(expected, result)
        expected = {"Gosho": []}
        result = library.books_by_authors
        self.assertEqual(expected, result)
