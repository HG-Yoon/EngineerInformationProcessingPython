lol = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(lol[0])  # [1, 2, 3]
print(lol[2][1])  # 7
for sub in lol:
    for item in sub:
        print(item, end=" ")
    print()

'''
출력결과
[1, 2, 3]
7
1 2 3
4 5
6 7 8 9
'''
