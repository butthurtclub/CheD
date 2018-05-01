__author__ = 'CheD'

import unittest

__all__ = (
    'Unit',
)


class UnitIsDead(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Unit:
    """
    A class for Unit representing.

    Usage:
    >>> unit = Unit('unit', 100, 20)
    >>> print(unit)
    Unit name: unit;
    Unit hp: 100;
    Unit damage: 20;
    >>> unit1 = Unit('unit1', 100, 20)
    >>> unit.attack(unit1)
    >>> unit1.attack(unit)
    >>> print(unit)
    Unit name: unit;
    Unit hp: 70.0;
    Unit damage: 20;
    >>> unit.add_hit_points(30)
    >>> print(unit)
    Unit name: unit;
    Unit hp: 100.0;
    Unit damage: 20;
    """
    def __init__(self, name, hp, dmg):
        """
        The initializer.

        :param name: Name of Unit. Possible value: string.
        :param hp:  Hit points of Unit. Possible value: integer, float.
        :param dmg: Damage power of Unit. Possible valu: integer, float.
        """
        self._name = name
        self._hit_points_limit = hp
        self._hit_points = hp
        self._damage = dmg

    def _ensure_is_alive(self):
        """
        Check. Is unit still alive?

        :raises: UnitIsDead: On self._hit_points == 0
        :return: None
        """
        if self._hit_points == 0:
            raise UnitIsDead('Unit is dead!')
        else:
            return None

    def __str__(self):
        return f'Unit name: {self.name};\nUnit hp: {self.hit_points};\nUnit damage: {self.damage};\n'

    @property
    def name(self):
        return self._name

    @property
    def hit_points(self):
        return self._hit_points

    @property
    def hit_points_limit(self):
        return self._hit_points_limit

    @property
    def damage(self):
        return self._damage

    @hit_points.setter
    def hit_points(self, hp):
        self._hit_points = hp

    def take_damage(self, dmg):
        """
        Unit take damage. (decrease hit_points)

        :param dmg: Damage of unit(attacker). Possible value: integer
        :return: None
        """
        self._ensure_is_alive()

        self.hit_points -= dmg

        if self.hit_points <= 0:
            self.hit_points = 0
            pass

    def add_hit_points(self, hp):
        """
        Increase hit_points.

        :param hp: Possible value: integer, float
        :return:None
        """
        self._ensure_is_alive()

        self.hit_points += hp

        if self.hit_points > self.hit_points_limit:
            self.hit_points = self.hit_points_limit
            pass

    def attack(self, other):
        """
        The attack method. Self unit attack other unit

        :param other: Will be attacked by self.unit and counter attack him. Possible value: class Unit
        :return: None
        """
        if other is not self:
            other.take_damage(self.damage)
            other.counter_attack(self)

    def counter_attack(self, other):
        """
        The counter attack method.

        :param other: Will hit the other unit with half of damage power.
        :return: None
        """
        other.take_damage(self.damage/2)


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
