from unittest import TestCase, main
from examp_prep.apr import Hero


class HeroTest(TestCase):

    def test_init_returns_proper(self):
        hero = Hero("Stoyan", 5, 20, 5)

        self.assertEqual("Stoyan", hero.username)
        self.assertEqual(5, hero.level)
        self.assertEqual(20, hero.health)
        self.assertEqual(5, hero.damage)

    def test_battle_raises_exception_for_same_name(self):
        hero = Hero("Stoyan", 5, 20, 5)
        enemy = Hero("Stoyan", 5, 20, 5)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_value_error_for_same_le_health(self):
        hero = Hero("Stoyan", 5, 0, 5)
        enemy = Hero("Ivan", 5, 20, 5)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raises_value_error_for_same_le_enemy_healh(self):
        hero = Hero("Stoyan", 5, 5, 5)
        enemy = Hero("Ivan", 5, -1, 5)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight Ivan. He needs to rest", str(ex.exception))

    def test_battle_return_draw(self):
        hero = Hero("Stoyan", 5, 5, 5)
        enemy = Hero("Ivan", 5, 5, 5)

        self.assertEqual("Draw", hero.battle(enemy))
        self.assertEqual(-20, hero.health)
        self.assertEqual(-20, enemy.health)

    def test_battle_return_you_win(self):
        hero = Hero("Stoyan", 5, 20, 5)
        enemy = Hero("Ivan", 3, 5, 3)

        self.assertEqual("You win", hero.battle(enemy))
        self.assertEqual(6, hero.level)
        self.assertEqual(16, hero.health)
        self.assertEqual(10, hero.damage)

    def test_battle_return_you_lose(self):
        hero = Hero("Stoyan", 3, 20, 3)
        enemy = Hero("Ivan", 3, 20, 4)

        self.assertEqual("You lose", hero.battle(enemy))
        self.assertEqual(4, enemy.level)
        self.assertEqual(16, enemy.health)
        self.assertEqual(9, enemy.damage)

    def test_str_hero_return_proper(self):
        hero = Hero("Stoyan", 3, 20, 3)
        result = hero.__str__()
        expected = f"Hero {hero.username}: {hero.level} lvl\n" \
                   f"Health: {hero.health}\n" \
                   f"Damage: {hero.damage}\n"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
