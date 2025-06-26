a = 100
result = 0
for i in range(1, 3):
    result = a >> i
    result = result+1
print(result)

'''
i=1,
result = 100 >> 1 = 100 / 1^2 = 100 / 1 = 100
result = 100 + 1 = 101

i=2,
result = 101 >> 2 = 101 / 2^2 = 101 / 4 = 25
result = 25 + 1 = 26

출력결과
26
'''
