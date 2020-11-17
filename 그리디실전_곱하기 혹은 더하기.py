#숫자로 된 문자열 입력받기
data = input()

#첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)) :
    #이 전 문자 다음 문자를 숫자로 변경하여 대입
    num = int(data[i])
    if num <=1 or result <=1 :
        result += num
    else :
        result *= num

print(result)
