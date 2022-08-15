class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTest(TestCase):

    def test_correct_name(self):
        worker = Worker("Ivan", 100, 5)
        result = f"{worker.name}, {worker.salary}, {worker.energy}"
        expected = "Ivan, 100, 5"
        self.assertEqual(result, expected)

    def test_energy_after_rest(self):
        worker = Worker("Ivan", 100, 5)
        result = worker.energy
        self.assertEqual(result, 5)

        worker.rest()
        result = worker.energy
        self.assertEqual(result, 6)

    def test_if_error_raises_with_less_or_equal_than_zero(self):
        worker = Worker("Ivan", 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_increase_after_work(self):
        worker = Worker("Ivan", 100, 5)
        self.assertEqual(worker.money, 0)
        worker.work()
        self.assertEqual(worker.money, 100)

    def test_energy_after_work(self):
        worker = Worker("Ivan", 100, 5)
        self.assertEqual(worker.energy, 5)
        worker.work()
        self.assertEqual(worker.energy, 4)

    def test_get_info(self):
        worker = Worker("Ivan", 100, 5)
        result = worker.get_info()
        expected = "Ivan has saved 0 money."
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
