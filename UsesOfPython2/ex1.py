a = [1, 2, 3, 4, 5]
x = 100
if x == 10:
    a = list(map(lambda num: num+10, a))
elif x == 50:
    a = list(map(lambda num: num+50, a))
else:
    a = list(map(lambda num: num+100, a))
    # a의 각 요소에 100을 더하는 람다 식을 적용한 후,
    # 100씩 더해진 값들을 다시 리스트로 구성하여 a에 저장한다.
print(a)  # [101, 102, 103, 104, 105]
