"""
Test class for ll2wm function
"""

import unittest
import numpy
from ocutils import earth_radius
from ocutils.ll2wm import ll2wm


class Testll2wm(unittest.TestCase):

    def setUp(self):
        self.tol = 1e-6

    def tearDown(self):
        pass

    def test_bounds(self):

        lat = numpy.array([-90])
        lon = numpy.array([-180])
        try:
            _, _ = ll2wm(lat, lon)
        except ValueError as ve:
            self.assertEqual(ve.__str__(), 'Latitude must be > -90 and < 90 degrees')

        lat = numpy.array([90])
        lon = numpy.array([-180])
        try:
            _, _ = ll2wm(lat, lon)
        except ValueError as ve:
            self.assertEqual(ve.__str__(), 'Latitude must be > -90 and < 90 degrees')

        lat = numpy.array([89])
        lon = numpy.array([-181])
        try:
            _, _ = ll2wm(lat, lon)
        except ValueError as ve:
            self.assertEqual(ve.__str__(), 'Longitude must be >= -180 and <= 180 degrees')

        lat = numpy.array([89])
        lon = numpy.array([181])
        try:
            _, _ = ll2wm(lat, lon)
        except ValueError as ve:
            self.assertEqual(ve.__str__(), 'Longitude must be >= -180 and <= 180 degrees')

    def test_zeros(self):

        lat = numpy.array([0])
        lon = numpy.array([0])
        x, y = ll2wm(lat, lon)
        self.assertAlmostEqual(x, 0, delta=self.tol)
        self.assertAlmostEqual(y, 0, delta=self.tol)

    def test_zero_lat(self):

        lat = numpy.array([0])
        lon = numpy.array([0])
        x, y = ll2wm(lat, lon, lon0=-180)
        self.assertAlmostEqual(x, numpy.pi * earth_radius, delta=self.tol)
        self.assertAlmostEqual(y, 0, delta=self.tol)

    def test_equal(self):

        lon = numpy.array([45])
        lat = numpy.rad2deg(2 * numpy.arctan(numpy.exp(numpy.deg2rad(lon))) - numpy.pi / 2)
        x, y = ll2wm(lat, lon)
        self.assertAlmostEqual(x, y, delta=self.tol)

    def test_two(self):

        lat = numpy.array([0, 45])
        lon = numpy.array([0, numpy.rad2deg(numpy.log(numpy.tan(numpy.pi / 4 + numpy.deg2rad(lat[1]) / 2)))])
        x, y = ll2wm(lat, lon)
        self.assertAlmostEqual(x[0], 0, delta=self.tol)
        self.assertAlmostEqual(y[0], 0, delta=self.tol)
        self.assertAlmostEqual(x[1], y[1], delta=self.tol)


if __name__ == '__main__':
    unittest.main()
