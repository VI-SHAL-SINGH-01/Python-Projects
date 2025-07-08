class one:
    x=10
    y=10
    def add(self):
        c=self.x+self.y
        print(c)
class second(one):
    def mul(self):
        c=self.x*self.y
        print(c)

k=second()
k.mul()
k.add()
