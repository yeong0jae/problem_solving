def solution(N, stages):
    
    answer = []
    
    for i in range(1, N+1):
        cnt = 0
        for stage in stages:
            if stage == i:
                cnt += 1
        if i == 1:
            answer.append(cnt / len(stages))
            lastlen = len(stages)
            lastcnt = cnt
        else:
            lastlen = lastlen - lastcnt # stages를 탐색하면서 이전 i에서의 결과를 활용
            lastcnt = cnt
            if lastlen == 0:
                answer.append(0)
            else : answer.append(cnt / lastlen)
        
    dic = {k : v for k, v in enumerate(answer)} # enumerate는 인덱스와 값의 쌍을 제공함 => list를 dict로
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    
    result = [a + 1 for a in sorted_dict.keys()]
    
    return result

# 더 나은 풀이

