# GEO-DISTRUBUTED LRU CACHE
A python library implementing a basic geo-distributed LRU (Least Recently Used) cache. The cache system allows for insertion, removal, complete deletion of data, peeking and entry count. The user is able to find the closest cache to his or her location (based on IP), and work with said closest cache. The most recent accessed or added data is kept at the front of the cache, and when the number of entries to the cache exceeds the defined size, the oldest data is removed from the cache. Additionally, every piece of data inputted is datestamped with the exact time of input.

## Dependencies
The library utilizes the requests, json, math, datettime, and collections libraries, all which are available within the Standard Python Library. It also utilizes the freegeoip API in order to handle the geo-distributed aspect.

## Usage
Import as: `import lru_cache`

Initializing a new cache: `lru_cache.Cache(latitude, longitude, size)`

Finding closest location cache: `lru_cache.get_closest_cache(lru_cache.caches)`

Insert to a cache: `cache.put(key, value)`

Get data from cache: `cache.get(key)`

Remove specified data: `cache.remove(key)`

View cache data: `cache.peek()`

Get number of items in cache: `cache.count()`

Wipe data from cache: `cache.delete()`

## Missing Functionality and Potential Improvements
This implementation serves as an extemely basic implementation of the given concept. As to what is missing from the implementation guidelines, this implementation lacks cache expiry. For proper functionality, the program would ideally store information in a better format (i.e SQL Database) and have a higher capicity. The program would also be much more efficient in a language other than Python, but for sake of consistancy and familiarity I chose to stick with it. Additionally, in a proper implementation I would personally avoid using the free geolocation API utilized within this library. While it works, I cannot speak to the accuracy and reliability of it long term. Additionally, we could replace the OrderedDict with a self-implemented data structure to reduce dependencies and increase flexibility.
