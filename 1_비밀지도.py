def solution(n, arr1, arr2): # 정사각형n, 지도 배열
    newarr1 = []
    newarr2 = []
    for a1 in arr1:
        a1 = bin(a1)[2:].zfill(n) # 2진수 변환 후 n자리로 채우기
        newarr1.append(a1)
    for a2 in arr2:
        a2 = bin(a2)[2:].zfill(n)
        newarr2.append(a2)
    
    newmap = []
    tmp = ""
    for i in range(n):
        for j in range(n):
            if newarr1[i][j] == "0" and newarr2[i][j] == "0": # if else로 00이면 공백, 아니면 #으로 채우기
                tmp += " "
            else:
                tmp += "#"
        newmap.append(tmp)
        tmp = ""

    return newmap

# 더 나은 풀이 - 비트 연산을 이용

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) # or 연산으로 00이면 0, 나머지는 1이 되도록 연산 후 저장
        a12=a12.rjust(n,'0') # n 자리로 채우기
        a12=a12.replace('1','#') # 1은 #으로
        a12=a12.replace('0',' ') # 0은 공백으로
        answer.append(a12)
    return answer
