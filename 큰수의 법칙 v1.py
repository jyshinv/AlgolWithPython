# n, m, k를 공백으로 구분하여 입력받기
# n은 배열의 크기, m은 숫자가 더해지는 횟수
# 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과할 수 없음(k번까지만 더해질 수 있음)
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))  # 공백으로 구분하여 입력 받고 list에 담기

data.sort()  # 오름차순으로 정렬하기(대입 필요 x)
first = data[n - 1]  # 가장 큰 수 (배열 제일 끝에 있는 수)
second = data[n - 2]  # 두번째로 큰 수 (배열 제일 끝에서 하나 앞에 있는 수)

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if m == 0:  # m=0이라면 반복문을 탈출해라
            break

        result += first
        m -= 1  # 더할 때마다 1씩 빼기

    if m == 0:  # m이 0이면 반복문 탈출
        break

    result += second  # 두번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)  # 최종 답안 출력

