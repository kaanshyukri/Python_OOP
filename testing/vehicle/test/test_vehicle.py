from unittest import TestCase, main
from examp_prep.apr import Vehicle


class VehicleTest(TestCase):

    def test_init_return_proper(self):
        vehicle = Vehicle(100, 60)
        self.assertEqual(vehicle.fuel, 100.0)
        self.assertEqual(vehicle.capacity, 100.0)
        self.assertEqual(vehicle.horse_power, 60.0)
        self.assertEqual(vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive_raises_exception(self):
        vehicle = Vehicle(100, 60)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(81)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_return_proper_fuel(self):
        vehicle = Vehicle(100, 60)
        vehicle.drive(50)
        self.assertEqual(37.5, vehicle.fuel)

    def test_refuel_raises_exception(self):
        vehicle = Vehicle(100, 60)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_return_proper_fuel(self):
        vehicle = Vehicle(100, 60)
        vehicle.drive(50)
        vehicle.refuel(60)
        self.assertEqual(97.5, vehicle.fuel)

    def test_str_method(self):
        vehicle = Vehicle(100, 60)
        result = vehicle.__str__()
        expected = f"The vehicle has {vehicle.horse_power} " \
                   f"horse power with {vehicle.fuel} fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()