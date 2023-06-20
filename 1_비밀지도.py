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
