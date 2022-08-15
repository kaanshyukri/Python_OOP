from project.train.train import Train
from unittest import TestCase, main


class TrainTest(TestCase):

    def test_init(self):

        train = Train("BDJ", 5)
        self.assertEqual("BDJ", train.name)
        self.assertEqual(5, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_raises_error_train_full(self):
        train = Train("BDJ", 2)
        train.passengers = ["Ivan", "Gosho"]
        with self.assertRaises(ValueError) as ex:
            train.add("Radi")
        self.assertEqual("Train is full", str(ex.exception))
        self.assertEqual(["Ivan", "Gosho"], train.passengers)

    def test_add_name_in_list(self):
        train = Train("BDJ", 3)
        train.passengers = ["Ivan", "Gosho"]
        with self.assertRaises(ValueError) as ex:
            train.add("Gosho")
        self.assertEqual("Passenger Gosho Exists", str(ex.exception))
        self.assertEqual(["Ivan", "Gosho"], train.passengers)

    def test_add_return_added(self):
        train = Train("BDJ", 3)
        train.passengers = ["Ivan", "Gosho"]
        result = train.add("Radi")
        expected = "Added passenger Radi"
        self.assertEqual(expected, result)
        self.assertEqual(["Ivan", "Gosho", "Radi"], train.passengers)

    def test_remove_name_not_in_list(self):
        train = Train("BDJ", 3)
        train.passengers = ["Ivan", "Gosho"]
        with self.assertRaises(ValueError) as ex:
            train.remove("Radi")
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(["Ivan", "Gosho"], train.passengers)

    def test_remove_name_in_list(self):
        train = Train("BDJ", 3)
        train.passengers = ["Ivan", "Gosho"]
        result = train.remove("Ivan")
        expected = "Removed Ivan"
        self.assertEqual(expected, result)
        self.assertEqual(["Gosho"], train.passengers)

        train.passengers.remove["Kaan"]


if __name__ == "__main__":
    main()