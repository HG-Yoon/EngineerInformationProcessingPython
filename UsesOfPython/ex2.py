a = {'apple', 'lemon', 'banana'}
a.update({'kiwi', 'banana'})  # {'apple','lemon','banana','kiwi'}
a.remove('lemon')  # {'apple','banana','kiwi'}
a.add('apple')  # {'apple','banana','kiwi'}
for i in a:
    print("과일명 : %s" % i)
'''
과일명 : apple
과일명 : banana
과일명 : kiwi
과일명 : banana
과일명 : apple
'''
