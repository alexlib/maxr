""" file: test_parameters.py
"""

from __future__ import print_function, division
import unittest

from maxr import Parameters

class TestParameters(unittest.TestCase):

    """ Check that parameters get updated ok
    """

    def setUp(self):
        self.p = Parameters()

    def test_setting(self):
        "Equivalent parameters should be updated at the same time"
        for p1, p2 in self.p.equivalent:
            self.p[p1] = 1
            self.assertEqual(1, self.p[p2])

    def test_defaults(self):
        "Defaults should remain set when not set already"
        for par, val in self.p.default_parameters.items():
            self.assertEqual(self.p[par], val)

    def test_attributes(self):
        "Attributes should be copied to the dictionary"
        for par, val in self.p.items():
            self.assertEqual(getattr(self.p, par), val)

    def test_unknown(self):
        "Adding an unknown key raises a KeyError"
        self.assertRaises(KeyError, lambda *a: self.p.__setitem__(*a),
                          'foo', 'bar')

if __name__ == '__main__':
    unittest.main()