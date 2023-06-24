def solution(cacheSize, cities): # 캐시 크기와 데이터가 주어짐
    answer = 0
    if cacheSize == 0: # 캐시 크기 0인경우 예외처리
        return 5 * len(cities)
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache: # cache hit 인 경우 실행시간 +1, (캐시 내에서 데이터 삭제, 추가이므로 실행시간 적은 것)
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) < cacheSize: # cache miss인 경우 실행시간 +5, (외부에서 캐시에 데이터 추가,삭제이므로 실행시간 큰 것)
                cache.append(city)
            elif len(cache) == cacheSize: # 이 경우 pop을 하고 append를 하기 때문에 cacheSize가 len(cache)보다 더 커지는 경우는 안 생김
                cache.pop(0)
                cache.append(city)
            answer += 5
    
    return answer

# 더 나은 풀이

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize) # maxlen을 준 deque에서는 가장 오래된 요소가 자동으로 제거(popleft)됨
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
