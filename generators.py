def gen(n):
    while n > 0:
        yield n
        n -= 1

for i in gen(3):
    print(i)

g = gen(3)
f = gen(10)
print(next(g))
print(next(f))

print(type(gen))
print(type(gen(3)))