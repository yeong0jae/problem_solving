def solution(s):
    
    for i in range(len(s)): # 선형탐색유형(알파벳을 모두 확인할 필요 없음), 10가지 케이스 모두 확인
        if s[i:i+2] == "on":
            s = s[:i] + "1" + s[i+3:]
        elif s[i:i+2] == "tw":
            s = s[:i] + "2" + s[i+3:]
        elif s[i:i+2] == "th":
            s = s[:i] + "3" + s[i+5:]
        elif s[i:i+2] == "fo":
            s = s[:i] + "4" + s[i+4:]
        elif s[i:i+2] == "fi":
            s = s[:i] + "5" + s[i+4:]
        elif s[i:i+2] == "si":
            s = s[:i] + "6" + s[i+3:]
        elif s[i:i+2] == "se":
            s = s[:i] + "7" + s[i+5:]
        elif s[i:i+2] == "ei":
            s = s[:i] + "8" + s[i+5:]
        elif s[i:i+2] == "ni":
            s = s[:i] + "9" + s[i+4:]
        elif s[i:i+2] == "ze":
            s = s[:i] + "0" + s[i+4:]
    
    answer = int(s)
    
    return answer
  
  
  
# 더 나은 풀이

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
# 1대1로 대응하여 대체할 것을 생각해서 딕셔너리 자료형 이용

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value) # key, value를 그대로 replace 함수에 이용
    return int(answer)
