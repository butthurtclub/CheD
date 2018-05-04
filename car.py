__author__ = 'CheD'

import unittest
import point

__all__ = (
    'Car',
)


class FuelException(Exception):
    """Base class for fuel exceptions"""
    pass


class OutOfFuel(FuelException):
    """The tank is empty.(fuel_amount == 0)"""
    pass


class ToMuchFuel(FuelException):
    """The tank is full.(fuel_amount == fuel_capacity)"""


class Car:
    """
    A class for Car representing.
    Use types: integer, floating, Point(), string.

    Usage:
    >>> car = Car()
    >>> print(car)
    Car model: Mercedes
    Location: (0, 0)
    Max fuel:60
    Fuel amount: 60
    >>> paris = point.Point(10, 10)
    >>> car.drive(paris) or car.drive(x=10, y=10)
    >>> print(car)
    Car model: Mercedes
    Location: (10, 10)
    Max fuel:60
    Fuel amount: 51.52
    """
    def __init__(self, fuel_capacity=60, fuel_consumption=0.6,
                 location=point.Point(), model='Mercedes'):
        """
        The initializer.

        :param fuel_capacity: Possible values: integer, float
        :param fuel_consumption: Possible values: integer, float
        :param location: Possible values: Point()
        :param model: Possible values: string
        """
        self._location = location
        self._fuel_amount = fuel_capacity
        self._model = model
        self._fuel_capacity = fuel_capacity
        self._fuel_consumption = fuel_consumption

    def __str__(self):
        return f'Car model: {self.model}\nLocation: {self.location}\n' \
               f'Max fuel:{self.fuel_capacity}\nFuel amount: {self.fuel_amount}'

    @property
    def fuel_amount(self):
        return round(self._fuel_amount, 2)

    @property
    def fuel_capacity(self):
        return self._fuel_capacity

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @property
    def location(self):
        return self._location

    @property
    def model(self):
        return self._model

    def refill(self, fuel):
        """
        Method that refills your car.

        :param fuel: Fuel need to add
        :raises ToMuchFuel: On refilling already full tank
        """
        if self.fuel_amount == self.fuel_capacity:
            raise ToMuchFuel('You already have full tank!')

        self._fuel_amount += fuel

        if self.fuel_amount > self.fuel_capacity:
            self._fuel_amount = self.fuel_capacity

    def drive(self, destination=None, **kwargs):
        """
        Car goes to the destination point

        :param destination: Possible values: Point().
        :param kwargs: Destination in form  x, y.
        :raises OutOfFuel: On not enough fuel
        """
        destination = destination or point.Point(**kwargs)

        trip_distance = self.location.distance(destination)
        fuel_need = trip_distance * self.fuel_consumption

        if fuel_need > self.fuel_amount:
            raise OutOfFuel('Not enough fuel! Please, refill your car.')

        self._location = destination
        self._fuel_amount -= fuel_need


class TestCar(unittest.TestCase):
    def test_default_car_create(self):
        car = Car()

        self.assertEqual(car.model, 'Mercedes')
        self.assertEqual(car.fuel_capacity, 60)
        self.assertEqual(car.fuel_amount, 60)
        self.assertEqual(car.location, point.Point(0, 0))
        self.assertEqual(car.fuel_consumption, 0.6)

    def test_other_car_create(self):
        car = Car(100, 0.9, point.Point(1, 1), 'Toyota')

        self.assertEqual(car.model, 'Toyota')
        self.assertEqual(car.fuel_capacity, 100)
        self.assertEqual(car.fuel_amount, 100)
        self.assertEqual(car.location, point.Point(1, 1))
        self.assertEqual(car.fuel_consumption, 0.9)

    def test_car_refill_and_drive(self):
        car = Car()
        paris = point.Point(30, 20)

        with self.assertRaises(ToMuchFuel):
            car.refill(1)

        self.assertEqual(car.model, 'Mercedes')
        self.assertEqual(car.fuel_capacity, 60)
        self.assertEqual(car.fuel_amount, 60)
        self.assertEqual(car.location, point.Point(0, 0))
        self.assertEqual(car.fuel_consumption, 0.6)

        car.drive(paris)

        self.assertEqual(car.model, 'Mercedes')
        self.assertEqual(car.fuel_capacity, 60)
        self.assertEqual(car.fuel_amount, 38.36)
        self.assertEqual(car.location, point.Point(30, 20))
        self.assertEqual(car.fuel_consumption, 0.6)

    def test_ride_without_fuel(self):
        car = Car(0, 0.6, point.Point(), 'Mercedes')

        self.assertEqual(car.fuel_amount, 0)

        with self.assertRaises(OutOfFuel):
            car.drive(x=1, y=1)

    def test_drive(self):
        car = Car()
        kiev = point.Point(10, 10)

        self.assertEqual(car.location, point.Point(0, 0))

        car.drive(kiev)

        self.assertEqual(car.location, point.Point(10, 10))

        car.drive(x=20, y=20)

        self.assertEqual(car.location, point.Point(20, 20))


if __name__ == '__main__':
    unittest.main()
