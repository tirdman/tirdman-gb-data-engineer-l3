from math import fsum
#
# from django import request

print('Test')




def generator():
    for el in (1, 2, 3):
        yield el

def generator2():
    g32 = (el for el in (1, 2, 3))
    return g32


g = generator()

for i in g:
    print(i)

print('---------')

g2 = generator2()
next(g2)


for i in g2:
    print(i)

[]
