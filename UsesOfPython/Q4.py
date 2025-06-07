a = 100
result = 0
for i in range(1, 3):
    result = a >> i
    result = result+1
print(result)  # 26
'''
i = 1,
100 >> 1 = 100 / 2^1 = 100 / 2 = 50
result = 50 + 1 = 51
i = 2,
100 >> 2 = 100 / 2^2 = 100 / 4 = 25
result = 25 + 1 = 26
'''
