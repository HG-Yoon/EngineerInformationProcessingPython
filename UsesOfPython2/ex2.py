class Cls:
    x, y = 10, 20

    def chg(self):
        temp = self.x
        self.x = self.y
        self.y = temp


a = Cls()
print(a.x, a.y)  # 10 20
a.chg()
print(a.x, a.y)  # 20 10
