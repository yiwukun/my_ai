"""
class Fibs:
    def __init__(self , n = 20):
        self.n1 = 0
        self.n2 = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.n1, self.n2 = self.n2, self.n1 + self.n2
        if(self.n1 > self.n):
            raise (StopIteration)
        return self.n1


for i in Fibs(20):
    print(i)
"""

def fibs():
    a = 0
    b = 1
    while True:
        a , b = b, a + b
        yield a

for i in fibs():
    if(i > 100):
        break
    print(i)