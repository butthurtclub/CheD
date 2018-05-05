__author__ = 'CheD'

__all__ = (
    'Unit',
    'UnitIsDead',
)


class UnitIsDead(Exception):
    pass


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
        """
        if self._hit_points == 0:
            raise UnitIsDead('Unit is dead!')

    def __str__(self):
        return f'Unit name: {self.name};\nUnit hp: {self.hit_points};\n' \
               f'Unit damage: {self.damage};\n'

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

    def take_damage(self, dmg):
        """
        Unit take damage. (decrease hit_points)

        :param dmg: Damage of unit(attacker). Possible value: integer
        """
        self._ensure_is_alive()

        self._hit_points -= dmg

        if self.hit_points <= 0:
            self._hit_points = 0

    def add_hit_points(self, hp):
        """
        Increase hit_points.

        :param hp: Possible value: integer, float
        """
        self._ensure_is_alive()

        self._hit_points += hp

        if self.hit_points > self.hit_points_limit:
            self._hit_points = self.hit_points_limit

    def attack(self, other):
        """
        The attack method. Self unit attack other unit

        :param other: Will be attacked by self.unit and counter attack him.
                      Possible value: class Unit
        """
        if other is not self:
            other.take_damage(self.damage)
            other.counter_attack(self)

    def counter_attack(self, other):
        """
        The counter attack method.

        :param other: Will hit the other unit with half of damage power.
        """
        other.take_damage(self.damage/2)
