import math

print('請選擇屬性模式(有屬性:1,無屬性:2)')
mode = int(input())
print('請輸入攻擊數值')
ATK = int(input())
print('請輸入腕力數值')
PWR = int(input())

DEF = 174
if mode == 1:
    print('請輸入魔力數值')
    MATK = int(input())
    BASE = (ATK-DEF/4)*(PWR/32+1)*3.25*(((10*MATK+16)**0.5-4)/64+1)
elif mode == 2:
    BASE = (ATK-DEF/4)*(PWR/32+1)*3.25

d1 = []
d2 = []
M = 0

print('請輸入傷害值')
rDMG = int(input())
for i in range(16,48):
    for M in range(0,1001):
        tDMG = math.floor((BASE+ATK*i/25.6)*0.01*M)
        if tDMG == rDMG:
            d1.append(M)

k = len(d1)
while k != 0 and k != 1:
    print('請輸入傷害值')
    rDMG = int(input())
    for i in range(16,48):
        for M in d1:
            tDMG = math.floor((BASE+ATK*i/25.6)*0.01*M)
            if tDMG == rDMG:
                d2.append(M)
    d1 = d2
    d2 = []
    k = len(d1)

if len(d1) == 0:
    print('error...')
elif len(d1) == 1:
    print('此技能倍率為'+str(d1[0])+'%')
input()