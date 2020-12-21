import requests
import json
import math
from datetime import datetime
from collections import OrderedDict

"""
Question C

At Ormuco, we want to optimize every bits of software we write.
Your goal is to write a new library that can be integrated to the Ormuco stack.
Dealing with network issues everyday, latency is our biggest problem. 
Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. 
This library will be used extensively by many of our services so it needs to meet the following criteria:

    1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema
    7 - Cache can expire
"""

class Cache:

    # initialize params
    def __init__(self, lat, lon, size):
        self.cache = OrderedDict()
        self.lat = lat
        self.lon = lon
        self.size = size
        
    # function to get data from cache
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            raise Exception('Requested key not found in cache')
    
    # function to add data to cache
    def put(self, key, value):
        self.cache[key] = [value, datetime.now().isoformat()]
        self.cache.move_to_end(key)

        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
    
    # function to get current size of cache
    def count(self):
        return len(self.cache)
    
    # function to view current data in cache
    def peek(self):
        return self.cache
    
    # function to remove data from cache
    def remove(self, key):
        del self.cache[key]
    
    def delete(self):
        cmd = input("Are you sure you want to delete cache data? (y/n)")
        if cmd == 'y':
            self.cache = OrderedDict()


# size given for testing
size = 5

# caches with coords for Montreal, Vancouver, and SF respectively
caches = [
    Cache(45.508888, -73.561668, size),
    Cache(49.246292, -123.116226, size),
    Cache(37.773972, -122.431297, size)
]

# function to get closest cache to user
def get_closest_cache(caches):

    # find geo location of user (temporary, may be better way that is not dependent on given API)
    loc_url = 'https://freegeoip.app/json/'
    r = requests.get(loc_url)
    lat = json.loads(r.text)['latitude']
    lon = json.loads(r.text)['longitude']
    
    # calculate closest cache to user
    closest = math.inf
    closest_cache = caches[0]
    for cache in caches:
        d1 = abs(cache.lat - lat)
        d2 = abs(cache.lon - lon)
        dist = math.sqrt(d1**2 + d2**2)
        
        if dist < closest:
            closest = dist
            closest_cache = cache

    return closest_cache


def main():
    cache = get_closest_cache(caches)
    cache.put(1,1)
    print(cache.peek()[1][0])
    


if __name__ == "__main__":
    main()
        
