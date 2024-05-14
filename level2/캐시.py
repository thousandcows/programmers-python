from collections import deque


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

    @staticmethod
    def solution_with_deque(cache_size: int, cities: list[str]) -> int:
        q, time = deque(maxlen=cache_size), 0
        cities = list(map(lambda x: x.lower(), cities))
        for city in cities:

            if city in q:
                q.remove(city)
                q.append(city)
                time += 1
            else:
                q.append(city)
                time += 5
        return time
