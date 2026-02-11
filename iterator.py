#itertors and generators

lst=[10,20,30,40,50,55]
ite=iter(lst)

print(ite.__next__())
print(ite.__next__())
print(ite.__next__()) 
print(next(ite))
print(next(ite))
print(next(ite))

