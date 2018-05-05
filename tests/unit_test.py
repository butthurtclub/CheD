import unittest
from src.unit import Unit
from src.unit import UnitIsDead


class TestUnit(unittest.TestCase):
    def test_unit_create(self):
        jack = Unit('Jack', 100, 20)

        self.assertEqual(jack.name, 'Jack')
        self.assertEqual(jack.hit_points, 100)
        self.assertEqual(jack.hit_points_limit, 100)
        self.assertEqual(jack.damage, 20)

    def test_unit_suicide(self):
        jack = Unit('Jack', 100, 120)

        jack.attack(jack)

        self.assertEqual(jack.name, 'Jack')
        self.assertEqual(jack.hit_points, 100)
        self.assertEqual(jack.hit_points_limit, 100)
        self.assertEqual(jack.damage, 120)

    def test_unit_attack(self):
        jack = Unit('Jack', 100, 20)
        bob = Unit('Bob', 100, 33)

        jack.attack(bob)

        self.assertEqual(jack.name, 'Jack')
        self.assertEqual(jack.hit_points, 83.5)
        self.assertEqual(jack.hit_points_limit, 100)
        self.assertEqual(jack.damage, 20)

        self.assertEqual(bob.name, 'Bob')
        self.assertEqual(bob.hit_points, 80)
        self.assertEqual(bob.hit_points_limit, 100)
        self.assertEqual(bob.damage, 33)

        bob.attack(jack)

        self.assertEqual(jack.name, 'Jack')
        self.assertEqual(jack.hit_points, 50.5)
        self.assertEqual(jack.hit_points_limit, 100)
        self.assertEqual(jack.damage, 20)

        self.assertEqual(bob.name, 'Bob')
        self.assertEqual(bob.hit_points, 70)
        self.assertEqual(bob.hit_points_limit, 100)
        self.assertEqual(bob.damage, 33)

    def test_attack_dead_unit(self):
        jack = Unit('Jack', 100, 20)
        bob = Unit('Bob', 100, 33)

        jack.take_damage(100)

        with self.assertRaises(UnitIsDead):
            bob.attack(jack)

    def test_add_hit_points(self):
        jack = Unit('Jack', 100, 20)

        jack.take_damage(50)

        self.assertEqual(jack.hit_points, 50)

        jack.add_hit_points(50)

        self.assertEqual(jack.hit_points, 100)

        jack.take_damage(100)

        with self.assertRaises(UnitIsDead):
            jack.add_hit_points(100)


if __name__ == '__main__':
    unittest.main()
