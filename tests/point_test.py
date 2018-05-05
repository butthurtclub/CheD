from dive.src.point import Point
import unittest


class TestPoint(unittest.TestCase):
    def test_types(self):
        point = Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

        point.x = 5.5
        point.y = 5.5

        self.assertEqual(point.x, 5.5)
        self.assertEqual(point.y, 5.5)

    def test_eq_ne(self):
        point = Point()
        point1 = Point(1, 5)
        point2 = Point(1, 5.0)

        self.assertEqual(point == point1, False)
        self.assertEqual(point1 == point2, True)
        self.assertEqual(point != point2, True)

    def test_distance(self):
        point = Point()
        point1 = Point(1, 5)

        self.assertEqual(point.distance(point1), 5.1)


if __name__ == '__main__':
    unittest.main()
