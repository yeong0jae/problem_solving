def solution(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
    
    l1 = []
    for i in range(len(str1)-1):
        if str1[i] in alphabet_list and str1[i+1] in alphabet_list:
            l1.append(str1[i]+str1[i+1])
    
    l2 = []
    for i in range(len(str2)-1):
        if str2[i] in alphabet_list and str2[i+1] in alphabet_list:
            l2.append(str2[i]+str2[i+1])
          
    l2c = l2.copy()
    
    interset = []
    unionset = []
    for a in l1: # 합집합 만들기
        if a in l2c:
            interset.append(a)
            l2c.remove(a)
    unionset = l1 + l2
    unionset_copy = unionset.copy()
    interset_copy = interset.copy()
    for a in unionset: # 교집합 만들기
        if a in interset_copy:
            unionset_copy.remove(a)
            interset_copy.remove(a)
    
    if len(unionset_copy) == 0 and len(interset) == 0:
        return 65536
    else: return int((len(interset)/len(unionset_copy))*65536)


# 더 나은 풀이

import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo]) # 중복제거된 교집합, 합집합 돌면서 해당 요소의 개수 누적 합 계산
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

