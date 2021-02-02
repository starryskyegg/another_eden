import math

print('請選擇計算模式(正常:1,弱點:2,耐性:3)')
mode = int(input())

DEF = 0
d1 = []
d2 = []

print('請輸入攻擊數值')
ATK = int(input())
print('請輸入腕力數值')
PWR = int(input())
if mode == 1:
    RST = 1
elif mode == 2:
    print('請輸入魔力數值')
    MATK = int(input())
    RST = (MATK+(2*MATK)**0.5)/512+1.85
elif mode == 3:
    RST = 0.25

print('請輸入傷害值')
rDMG = int(input())
for i in range(16,48):
    while DEF <= ATK*2:
        tDMG = math.floor(math.floor((ATK-DEF/2)*(PWR/32+1)*1.75+ATK*i/25.6)*RST)
        if tDMG == rDMG:
            d1.append(DEF)
        DEF+=1
    DEF = 0

k = len(d1)
while k != 1:
    j = 0
    print('請輸入傷害值')
    rDMG = int(input())
    for i in range(16,48):
        for DEF in d1:
            tDMG = math.floor(math.floor((ATK-DEF/2)*(PWR/32+1)*1.75+ATK*i/25.6)*RST)
            if tDMG == rDMG:
                d2.append(DEF)
    d1 = d2
    d2 = []
    k = len(d1)
print('敵方的物防是'+str(d1[0]))
input()