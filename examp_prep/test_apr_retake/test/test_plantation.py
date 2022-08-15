from test_apr_retake.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):

    def test_init(self):
        plant = Plantation(5)
        self.assertEqual(5, plant.size)
        self.assertEqual({}, plant.plants)
        self.assertEqual([], plant.workers)

    def test_size_raises_error_negative_number(self):
        with self.assertRaises(ValueError) as ex:
            plant = Plantation(-3)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker(self):
        plant = Plantation(5)
        self.assertEqual("Ivan successfully hired.",plant.hire_worker("Ivan"))
        self.assertEqual(["Ivan"], plant.workers)

    def test_hire_worker_raiser_error(self):
        plant = Plantation(5)
        plant.hire_worker("Ivan")
        with self.assertRaises(ValueError) as ex:
            plant.hire_worker("Ivan")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_len(self):
        plant = Plantation(5)
        plant.plants = {"Flower1": [1, 2, 3], "Flower2": [1, 2]}
        result = plant.__len__()
        expected = 5
        self.assertEqual(expected, result)

    def test_planting_raises_error_worker_not_in_list(self):
        plant = Plantation(5)
        with self.assertRaises(ValueError) as ex:
            plant.planting("Ivan", "Flower")
        self.assertEqual("Worker with name Ivan is not hired!", str(ex.exception))

    def test_planting_raiser_error_self_bigger_than_size(self):
        plant = Plantation(5)
        plant.plants = {"Ivan": [1, 2, 3], "Gosho": [1, 2]}
        plant.workers.append("Ivan")
        with self.assertRaises(ValueError) as ex:
            plant.planting("Ivan", "Flower")
        self.assertEqual("The plantation is full!", str(ex.exception))
        plant.plants = {"Ivan": [1, 2, 3], "Gosho": [1, 2, 5]}
        with self.assertRaises(ValueError) as ex:
            plant.planting("Ivan", "Flower")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_worker_in_dict(self):
        plant = Plantation(5)
        plant.workers = ["Ivan"]
        plant.plants = {"Ivan": ["rose", "blue"]}
        result = plant.planting("Ivan", "new_rose")
        expected = "Ivan planted new_rose."
        self.assertEqual(expected, result)
        self.assertEqual(["Ivan"], plant.workers)
        self.assertEqual({"Ivan": ["rose", "blue", "new_rose"]}, plant.plants)

    def test_planting_worker_in_list_but_not_in_dict(self):
        plant = Plantation(5)
        plant.workers.append("Gosho")
        result = plant.planting("Gosho", "rose")
        expected = "Gosho planted it's first rose."
        self.assertEqual(expected, result)
        self.assertEqual({"Gosho": ["rose"]}, plant.plants)
        self.assertEqual(["Gosho"], plant.workers)

    def test_str(self):
        plant = Plantation(5)
        plant.workers = ["Ivan", "Gosho"]
        plant.plants = {"Ivan": ["white", "blue"], "Gosho": ["green", "black"]}
        result = plant.__str__()
        expected = ["Plantation size: 5"]
        names = ["Ivan", "Gosho"]
        expected.append(', '.join(names))
        expected.append("Ivan planted: white, blue")
        expected.append("Gosho planted: green, black")

        self.assertEqual('\n'.join(expected), result)

    def test_repr(self):
        plant = Plantation(6)
        plant.workers = ["Ivan", "Gosho"]
        expected = "Size: 6\n" \
                   "Workers: Ivan, Gosho"
        result = plant.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()