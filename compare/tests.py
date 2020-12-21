import unittest
from compare import VersionCompare

class CompareTests(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(VersionCompare('1.2', '1.2').equal(), 'Versions are equal')
    
    def test_equal_2(self):
        self.assertEqual(VersionCompare('1.2', '1.2.0').equal(), 'Versions are equal')
    
    def test_not_equal_1(self):
        self.assertEqual(VersionCompare('1.2', '1.3').equal(), 'Versions are not equal')

    def test_not_equal_2(self):
        self.assertEqual(VersionCompare('1.2', '1.2.3').equal(), 'Versions are not equal')

    def test_gt_1(self):
        self.assertEqual(VersionCompare('1.2', '1.3').greater(), '1.3 is greater than 1.2')

    def test_gt_2(self):
        self.assertEqual(VersionCompare('1.3', '1.2').greater(), '1.3 is greater than 1.2')

    def test_gt_3(self):
        self.assertEqual(VersionCompare('1.2.2', '1.2').greater(), '1.2.2 is greater than 1.2')

    def test_lt_1(self):
        self.assertEqual(VersionCompare('1.2', '1.3').less(), '1.2 is less than 1.3')

    def test_lt_2(self):
        self.assertEqual(VersionCompare('1.3', '1.2').less(), '1.2 is less than 1.3')

    def test_lt_3(self):
        self.assertEqual(VersionCompare('1.2.2', '1.2').less(), '1.2 is less than 1.2.2')
    
    def test_invalid(self):
        with self.assertRaises(ValueError):
            VersionCompare('wrong entry', '1.2').equal()


if __name__ == "__main__":
    unittest.main()
