from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTest(TestCase):

    def test_init(self):
        bookstore = Bookstore(5)
        self.assertEqual(5, bookstore.books_limit)
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore.total_sold_books)

    def test_book_limit_raises_error_negative_number(self):
        bookstore = Bookstore(5)
        with self.assertRaises(ValueError) as ex:
            bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_len(self):
        bookstore = Bookstore(5)
        bookstore.availability_in_store_by_book_titles = {"5am": 3, "Friends": 5, "Enemy": 1, "Money": 0}
        self.assertEqual(9, len(bookstore))
        self.assertEqual({"5am": 3, "Friends": 5, "Enemy": 1, "Money": 0}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, bookstore.availability_in_store_by_book_titles["5am"])

    def test_receive_book_raises_error_greater_than_books_limit(self):
        bookstore = Bookstore(9)
        bookstore.availability_in_store_by_book_titles = {"5am": 3, "Friends": 5, "Enemy": 1}
        with self.assertRaises(Exception) as ex:
            bookstore.receive_book("Money", 3)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual({"5am": 3, "Friends": 5, "Enemy": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertNotIn("Money", bookstore.availability_in_store_by_book_titles)
        self.assertIn("5am", bookstore.availability_in_store_by_book_titles)

    def test_receive_book_book_title_not_in_dict(self):
        bookstore = Bookstore(15)
        bookstore.availability_in_store_by_book_titles = {"5am": 5, "Friends": 5, "Enemy": 2}
        result = bookstore.receive_book("Money", 3)
        expected = "3 copies of Money are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual({"5am": 5, "Friends": 5, "Enemy": 2, "Money": 3}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(15, len(bookstore))
        self.assertEqual(0, bookstore.total_sold_books)
        self.assertIn("Money", bookstore.availability_in_store_by_book_titles)

    def test_receive_book_book_in_dict(self):
        bookstore = Bookstore(20)
        bookstore.availability_in_store_by_book_titles = {"5am": 3, "Friends": 5, "Enemy": 1}
        result = bookstore.receive_book("5am", 3)
        expected = "6 copies of 5am are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual(6, bookstore.availability_in_store_by_book_titles["5am"])
        self.assertEqual(0, bookstore.total_sold_books)
        self.assertEqual(12, len(bookstore))

    def test_sell_book_title_not_in_dict(self):
        bookstore = Bookstore(20)
        bookstore.availability_in_store_by_book_titles = {"5am": 3, "Friends": 5, "Enemy": 1}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Money", 5)
        self.assertEqual("Book Money doesn't exist!", str(ex.exception))
        self.assertEqual(0, bookstore.total_sold_books)
        self.assertEqual({"5am": 3, "Friends": 5, "Enemy": 1}, bookstore.availability_in_store_by_book_titles)

    def test_sell_book_number_greater_than_value_raises_error(self):
        bookstore = Bookstore(20)
        bookstore.availability_in_store_by_book_titles = {"5am": 3, "Friends": 5, "Enemy": 1}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("5am", 5)
        self.assertEqual("5am has not enough copies to sell. Left: 3", str(ex.exception))
        self.assertEqual({"5am": 3, "Friends": 5, "Enemy": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(9, len(bookstore))

    def test_sell_book_return_text(self):
        bookstore = Bookstore(20)
        bookstore.availability_in_store_by_book_titles = {"5am": 3, "Friends": 5, "Enemy": 1}
        result = bookstore.sell_book("Friends", 5)
        expected = "Sold 5 copies of Friends"
        self.assertEqual(expected, result)
        self.assertEqual({"5am": 3, "Friends": 0, "Enemy": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, bookstore.total_sold_books)
        result = bookstore.sell_book("5am", 3)
        expected = "Sold 3 copies of 5am"
        self.assertEqual(expected, result)
        self.assertEqual(8, bookstore.total_sold_books)
        self.assertEqual({"5am": 0, "Friends": 0, "Enemy": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(1, len(bookstore))

    def test_str(self):
        bookstore = Bookstore(20)
        bookstore.availability_in_store_by_book_titles = {"5am": 3, "Friends": 5, "Enemy": 3}
        bookstore.sell_book("Friends", 4)
        bookstore.sell_book("5am", 2)
        bookstore.receive_book("5am", 4)
        result = str(bookstore)
        expected = "Total sold books: 6\n" \
                   "Current availability: 9\n" \
                   " - 5am: 5 copies\n" \
                   " - Friends: 1 copies\n" \
                   " - Enemy: 3 copies"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
