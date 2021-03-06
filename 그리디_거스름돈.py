
"""
그리디 알고리즘

    -거스름돈 예제와 그리디 알고리즘
    └'가장 큰 화폐 단위부터' 돈을 거슬러준다.
    ex) 500원/100원/50원/10원이 있고 1260원을 거슬러주려면?
    => 500 500 100 100 50 10 순서로 거슬러 주면 된다.

"""

n = 1260
count = 0

#거스름돈
coin_types = [500, 100, 50, 10]

for coin in coin_types : #in : 500 -> 100 -> 50 -> 10
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    # //연산자 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
    #위 코드에서 +=연산자가 가장 우선순위가 낮음
    n %= coin

print(count)