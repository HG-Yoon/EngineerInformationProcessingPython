def func(lst):
    for i in range(len(lst)//2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]


'''
i=0일 때,
lst[0],list[-1]=list[-1],lst[0]
1,2=2,1
[2,1,3,4,5,6]
i=1일 때,
lst[1],lst[-2]=lst[-2],lst[1]
1,3=3,1
[2,3,1,4,5,6]
i=2일 때,
lst[2],lst[-3]=lst[-3],lst[2]
1,4=4,1
[2,3,4,1,5,6]
'''
lst = [1, 2, 3, 4, 5, 6]
func(lst)
print(sum(lst[::2])-sum(lst[1::2]))  # 5-2=3
