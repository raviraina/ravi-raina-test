import unittest
from overlap import overlap

class OverlapTests(unittest.TestCase):

    def test_pos_pos_overlap(self):
        self.assertEqual(overlap((1,3),(2,6)), True)
    
    def test_neg_pos_overlap(self):
        self.assertEqual(overlap((-5,5),(-3,3)), True)

    def test_neg_neg_overlap(self):
        self.assertEqual(overlap((-6,-3),(-5,-1)), True)
    
    def test_same_pos_pos_overlap(self):
        self.assertEqual(overlap((4,8),(4,8)), True)
    
    def test_same_neg_neg_overlap(self):
        self.assertEqual(overlap((-8,-4),(-8,-4)), True)
    
    def test_same_neg_pos_overlap(self):
        self.assertEqual(overlap((-4,8),(-4,8)), True)
    
    def test_pos_pos_independent(self):
        self.assertEqual(overlap((2,3),(5,9)), False)

    def test_neg_post_independent(self):
        self.assertEqual(overlap((-5,2), (3,4)), False)
    
    def test_neg_neg_independent(self):
        self.assertEqual(overlap((-6,-3),(-2,-1)), False)
    
    def test_same_reflected_independent(self):
        self.assertEqual(overlap((-6,-3),(3,6)), False)
    
    def test_wrong_order_independent(self):
        self.assertEqual(overlap((-3,-6),(3,6)), False)
    
    def test_invalid_point(self):
        with self.assertRaises(ValueError):
            overlap((1,2,3), (3,6))



if __name__ == "__main__":
    unittest.main()