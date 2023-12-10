import math

def solution(n, k): # 정수 n과 k진수
    
    digits = [] # 진수 변환 시 저장할 리스트
    
    while n > 0:
        r = n % k
        digits.append(str(r)) # 나머지 추가
        n //= k
    
    digits.reverse() # 뒤집기
    
    s = ''.join(digits)
    
    sl = s.split('0') # 0 기준 split
    
    cnt = 0
    for i in sl: # 각각의 수가 소수인지 판별
        if i == '':
            continue
        
        if ispn(int(i)) == True:
            cnt += 1
    
    return cnt


def ispn(s): # 소수인지 판별 메소드. sqrt(n)까지 나머지가 0으로 나눠지는 수가 있으면 소수가 아님.
    if s <= 1:
        return False
    for j in range(2, int(math.sqrt(s)) + 1):
        if s % j == 0:
            return False
    return True


    
