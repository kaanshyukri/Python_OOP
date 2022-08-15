from aqua_shop import PetShop
from unittest import TestCase, main


class PetshopTest(TestCase):

    def test_init(self):
        petshop = PetShop("Reksi")
        self.assertEqual("Reksi", petshop.name)
        self.assertEqual({}, petshop.food)
        self.assertEqual([], petshop.pets)

    def test_add_food_raises_error_quantity_negative(self):
        petshop = PetShop("Reksi")
        with self.assertRaises(ValueError) as ex:
            petshop.add_food("Djoni", -2)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_name_not_in_list(self):
        petshop = PetShop("Reksi")
        result = petshop.add_food("Djoni", 5)
        expected = f"Successfully added 5.00 grams of Djoni."
        self.assertEqual(expected, result)
        self.assertEqual({"Djoni": 5}, petshop.food)

    def test_add_food_name_in_list(self):
        petshop = PetShop("Reksi")
        petshop.food["Djoni"] = 3
        result = petshop.add_food("Djoni", 10)
        expected = f"Successfully added 10.00 grams of Djoni."
        self.assertEqual(expected, result)
        self.assertEqual({"Djoni": 13}, petshop.food)

    def test_add_pet_raise_error_name_in_pet(self):
        petshop = PetShop("Reksi")
        petshop.pets = ["Djoni", "Reksi"]
        with self.assertRaises(Exception) as ex:
            petshop.add_pet("Reksi")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["Djoni", "Reksi"], petshop.pets)

    def test_add_pet_while_not_in_pets(self):
        petshop = PetShop("Reksi")
        petshop.pets = ["Djoni", "Reksi"]
        result = petshop.add_pet("Cheri")
        expected = "Successfully added Cheri."
        self.assertEqual(expected, result)
        self.assertEqual(["Djoni", "Reksi", "Cheri"], petshop.pets)

    def test_feed_pet_raises_error_pet_not_in_list(self):
        petshop = PetShop("Reksi")
        petshop.pets = ["Djoni", "Reksi"]
        with self.assertRaises(Exception) as ex:
            petshop.feed_pet("Granula", "Cheri")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_name_not_in_food(self):
        petshop = PetShop("Reksi")
        petshop.pets = ["Djoni", "Reksi"]
        result = petshop.feed_pet("Granul", "Djoni")
        expected = 'You do not have Granul'
        self.assertEqual(expected, result)

    def test_pet_food_quantity_below_100(self):
        petshop = PetShop("Reksi")
        petshop.pets = ["Djoni", "Reksi"]
        petshop.food["Granul"] = 6
        result = petshop.feed_pet("Granul", "Reksi")
        expected = "Adding food..."
        self.assertEqual(expected, result)
        self.assertEqual({"Granul": 1006}, petshop.food)

    def test_pet_food_successfully_fed(self):
        petshop = PetShop("Reksi")
        petshop.pets = ["Djoni", "Reksi"]
        petshop.food["Granul"] = 156
        result = petshop.feed_pet("Granul", "Reksi")
        expected = "Reksi was successfully fed"
        self.assertEqual(expected, result)
        self.assertEqual({"Granul": 56}, petshop.food)

    def test_repr(self):
        petshop = PetShop("Reksi")
        petshop.pets = ["Djoni", "Reksi", "Cheri"]
        result = petshop.__repr__()
        expected = f"Shop Reksi:\n" \
                   f"Pets: Djoni, Reksi, Cheri"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
