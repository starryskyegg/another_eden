import math

print('請輸入對方速度')
eSPD = int(input())

eMAX = math.floor(1.1*eSPD)
eMIN = math.floor(0.9*eSPD)
MIN = eMAX
MAX = eMIN

i = 0
while i == 0:
    if math.floor(0.9*MIN) == eMAX:
        print('要穩定超車速度至少要'+str(MIN+1))
        i = 1
    elif math.floor(0.9*MIN) > eMAX:
        print('要穩定超車速度至少要'+str(MIN))
        i = 1
    else:
        MIN+=1

i = 0
while i == 0:
    if math.floor(1.1*MAX) == eMIN:
        print('要穩定落後速度最多只能是'+str(MAX-1))
        i = 1
    elif math.floor(1.1*MAX) < eMIN:
        print('要穩定落後速度最多只能是'+str(MAX))
        i = 1
    else:
        MAX-=1
input()