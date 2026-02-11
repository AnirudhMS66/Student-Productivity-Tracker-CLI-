#itertors and generators

lst=[10,20,30,40,50,55]
ite=iter(lst)

print(ite.__next__())
print(ite.__next__())
print(ite.__next__()) 
print(next(ite))
print(next(ite))
print(next(ite))

class count:
    def __init__(self,max):
        self.num=0
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<self.max:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

c=count(3);
print(next(c))
print(next(c))
print(next(c))


def display():
    for i in range(0,3):
        yield i
d=display()
print(d.__next__())
print(next(d))
print(next(d))