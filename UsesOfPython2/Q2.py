def func(value):
    if type(value) == type(100):
        return 100
    elif type(value) == type(""):
        return len(value)
    else:
        return 20


a = "100.0"
b = 100.0
c = (100, 200)
print(func(a)+func(b)+func(c))  # 45
'''
func(a)=len(a)=5
func(b)=20
func(c)=20
func(a)+func(b)+func(c)=5+20+20=45
'''
