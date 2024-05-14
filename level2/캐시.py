class Cache:
    @staticmethod
    def solution(cache_size: int, cities: list[str]) -> int:

        if cache_size == 0:
            return len(cities) * 5

        cities = list(map(lambda x: x.lower(), cities))
        cache, total_time = {}, 0
        for i, city in enumerate(cities):
            if cache.get(city, -1) == -1:
                if len(cache) == cache_size:
                    cache = dict(sorted(cache.items(), key=lambda item: item[1], reverse=True))
                    cache.popitem()
                total_time += 5
            else:
                total_time += 1

            cache[city] = i
        return total_time
