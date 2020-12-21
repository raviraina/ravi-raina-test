import unittest
import lru_cache
from collections import OrderedDict
from datetime import datetime

class CacheTests(unittest.TestCase):

    def test_closest_cache(self):
        lat = lru_cache.get_closest_cache(lru_cache.caches).lat
        lon = lru_cache.get_closest_cache(lru_cache.caches).lon
        self.assertEqual(lat, 49.246292)
        self.assertEqual(lon, -123.116226)
    
    def test_put_cache(self):
        cache = lru_cache.get_closest_cache(lru_cache.caches)
        cache.put(1,4)
        self.assertEqual(cache.peek()[1][0], 4)

    def test_get_cache(self):
        cache = lru_cache.get_closest_cache(lru_cache.caches)
        cache.put(1,4)
        self.assertEqual(cache.get(1)[0], 4)
    
    def test_lru_aspect(self):
        cache = lru_cache.get_closest_cache(lru_cache.caches)
        
        # given cache size of 5, (0,0) should be removed and throw exception when get called
        for i in range(6):
            cache.put(i, i)
        
        with self.assertRaises(Exception):
            cache.get(0)
        




if __name__ == "__main__":
    unittest.main()

