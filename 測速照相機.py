import math

print('請選擇計算模式(正常:1,弱點:2,耐性:3)')
mode = int(input())

print('請輸入攻擊數值')
ATK = int(input())
print('請輸入腕力數值')
PWR = int(input())
print('請輸入魔力數值')
MATK = int(input())
print('請輸入速度數值')
SPD = int(input())
print('請輸入敵方物防值')
DEF = int(input())

if mode == 1:
    RST = 1
elif mode == 2:
    RST = (MATK+(2*MATK)**0.5)/512+1.85
elif mode == 3:
    RST = 0.25

eSPDmin = math.ceil(SPD/5)
eSPD = eSPDmin
d1 = []
d2 = []

BASE = (ATK-DEF/4)*(PWR/32+1)*3.25*(((10*MATK+16)**0.5-4)/64+1)

print('請輸入傷害值')
rDMG = int(input())
for i in range(16,48):
    while eSPD <= SPD:
        M = 0.01*math.floor(200*SPD/eSPD)
        tDMG = math.floor(math.floor((BASE+ATK*i/25.6)*M)*RST)
        if tDMG == rDMG:
            d1.append(eSPD)
        eSPD+=1
    eSPD = eSPDmin

k = len(d1)
while k != 1:
    print('請輸入傷害值')
    rDMG = int(input())
    for i in range(16,48):
        for eSPD in d1:
            M = 0.01*math.floor(200*SPD/eSPD)
            tDMG = math.floor(math.floor((BASE+ATK*i/25.6)*M)*RST)
            if tDMG == rDMG:
                d2.append(eSPD)
    d1 = d2
    d2 = []
    k = len(d1)
print('敵方的速度是'+str(d1[0]))
input()