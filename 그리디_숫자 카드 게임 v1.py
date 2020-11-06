#행의 개수 n과 열의 개수 m 공백 구분하여 입력받기
n,m = map(int, input().split())

#한줄 씩 입력받아 확인하기
result = 0
for i in range(n) :
    data = list(map(int, input().split()))

    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)

    #result에 누적하며 가장 큰 수 찾기
    #result에 저장된 max값과 새로 생긴 min_value 비교해서 제일 큰 값 추출
    result = max(result,min_value)

#최종 답안 출력
print(result)

