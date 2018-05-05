from dive.src.car import Car
from dive.src.car import OutOfFuel
from dive.src.car import ToMuchFuel

import unittest


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
