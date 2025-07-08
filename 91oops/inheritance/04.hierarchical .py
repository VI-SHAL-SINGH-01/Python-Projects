class one:
    x=10
    y=10
    def add(self):
        c=self.x+self.y
        print(c)
class second():
    def mul(self):
        c=self.x*self.y
        print(c)
class third(one,second):
    def divide(self):
        c=self.x/self.y
        print(c)

k=third()
k.add()
k.mul()