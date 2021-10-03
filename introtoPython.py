# rectangular area
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

difference1 = (x2-x1) * (y2-y1)
print(difference1)


#average number
a = int(input())
b = int(input())
c = int(input())
d = (a+b+c)/3
print(d)

# power raised to power of n
X  = int(input())
N = int(input())
cal = X**N
print(cal)

# Arithmetic Progression
a1, a2, a3 = int(input()) , int(input()), int(input())
d1 = a2 - a1
d2 = a3 - a2
if d1 == d2:
    print(d1)
