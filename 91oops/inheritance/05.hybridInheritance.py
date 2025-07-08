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
class third(one):
    def divide(self):
        c=self.x/self.y
        print(c)
class four(second,third):
    def subtract(self):
        c=self.x=self.y
        print(c)
k=four()
k.mul()
k.divide()
k.subtract()
k.add()
