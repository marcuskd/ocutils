import unittest

from ocutils.calc_haversine_dist import calc_haversine_dist


class TestCalcHaversineDist(unittest.TestCase):

    def test(self):

        """
        Tests against default case from online calculator at https://www.movable-type.co.uk/scripts/latlong.html
        """

        lat1 = 50 + 3 / 60 + 59 / 3600
        lon1 = 5 + 42 / 60 + 53 / 3600
        lon1 = -lon1
        lat2 = 58 + 38 / 60 + 38 / 3600
        lon2 = 3 + 4 / 60 + 12 / 3600
        lon2 = -lon2

        d = calc_haversine_dist(lat1, lon1, lat2, lon2)

        d_test = 968.9

        self.assertAlmostEqual(d / 1000, d_test, places=1)


if __name__ == '__main__':
    unittest.main()
