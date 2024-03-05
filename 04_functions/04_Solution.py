import math
def circle(r):
    area = math.floor(math.pi*r**2)
    circum = math.floor(2*math.pi*r)
    return area ,circum

a,c= circle(4)
print(a,c)