"""
Test class for wm2ll function
"""

import unittest
import numpy
from ocutils import earth_radius
from ocutils.wm2ll import wm2ll


class Testwm2ll(unittest.TestCase):

    def setUp(self):
        self.tol = 1e-6

    def tearDown(self):
        pass

    def test_zeros(self):

        x = numpy.array([0])
        y = numpy.array([0])
        lat, lon = wm2ll(x, y)
        self.assertAlmostEqual(lat, 0, delta=self.tol)
        self.assertAlmostEqual(lon, 0, delta=self.tol)

    def test_zero_lat(self):

        x = numpy.array([-numpy.pi * earth_radius])
        y = numpy.array([0])
        lat, lon = wm2ll(x, y)
        self.assertAlmostEqual(lat, 0, delta=self.tol)
        self.assertAlmostEqual(lon, -180, delta=self.tol)

    def test_equal(self):

        x = y = 2e6  # Arbitrary
        lat, lon = wm2ll(x, y)
        lat_test = numpy.rad2deg(2 * numpy.arctan(numpy.exp(numpy.deg2rad(lon))) - numpy.pi / 2)
        self.assertAlmostEqual(lat, lat_test, delta=self.tol)

    def test_two(self):

        x = numpy.array([0, 2e6])
        y = numpy.array([0, 2e6])
        lat, lon = wm2ll(x, y)
        lon1_test = numpy.rad2deg(numpy.log(numpy.tan(numpy.pi / 4 + numpy.deg2rad(lat[1]) / 2)))
        self.assertAlmostEqual(lat[0], 0, delta=self.tol)
        self.assertAlmostEqual(lon[0], 0, delta=self.tol)
        self.assertAlmostEqual(lon[1], lon1_test, delta=self.tol)


if __name__ == '__main__':
    unittest.main()
