def solution(s):
    
    s = s.lstrip('{').rstrip('}').split('},{') # 문자열 리스트를 진짜 리스트로 변환. replace나 strip, split 활용
    li = []
    for i in s:
      li.append(i.split(","))
    
    li = sorted(li, key=len)
    
    result = []
    
    for a in li:
        for aa in a:
            if aa not in result: # 정렬 후 2차원 배열 전체를 탐색하며 result에 없으면 삽입
                result.append(aa)
    
    return result

# 더 나은 풀이
