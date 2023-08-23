import unittest

from ocutils.calc_lat_lon import calc_lat_lon


class TestCalcLatLon(unittest.TestCase):

    def test(self):

        """
        Tests against default case from online calculator at https://www.movable-type.co.uk/scripts/latlong.html
        """

        slat = 53 + 19 / 60 + 14 / 3600
        slon = 1 + 43 / 60 + 47 / 3600
        slon = -slon
        theta = 96 + 1 / 60 + 18 / 3600
        r = 124.8 * 1000

        lat_test = 53 + 11 / 60 + 18 / 3600
        lon_test = 8 / 60

        lat, lon = calc_lat_lon(slat, slon, r, theta)

        self.assertAlmostEqual(lat, lat_test, places=3)
        self.assertAlmostEqual(lon, lon_test, places=3)


if __name__ == '__main__':
    unittest.main()
