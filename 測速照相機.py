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

d1 = []
d2 = []
BASE = (ATK-DEF/4)*(PWR/32+1)*3.25*(((10*MATK+16)**0.5-4)/64+1)

print('請輸入傷害值')
rDMG = int(input())
for i in range(16,48):
    for M in range(200,1001):
        tDMG = math.floor(math.floor((BASE+ATK*i/25.6)*0.01*M)*RST)
        if tDMG == rDMG:
            d1.append(M)

k = len(d1)
while k != 0 and k != 1:
    print('請輸入傷害值')
    rDMG = int(input())
    for i in range(16,48):
        for M in d1:
            tDMG = math.floor(math.floor((BASE+ATK*i/25.6)*0.01*M)*RST)
            if tDMG == rDMG:
                d2.append(M)
    d1 = d2
    d2 = []
    k = len(d1)

eSPD = 0
p = []
if len(d1) == 0:
    print('error...')
elif len(d1) == 1:
    M = d1[0]
    if M == 200:
        print('敵方太快了，請拉高速度再測')
    elif M == 1000:
        print('敵方太慢了，請降低速度再測')
    else:
        for eSPD in range(math.ceil(SPD/5),SPD+1):
            if math.floor(200*SPD/eSPD) == M:
                p.append(eSPD)
        if len(p) == 1:
            print('敵方的速度是'+str(p[0]))
        else:
            print('敵方的速度可能是')
            for eSPD in p:
                print(eSPD)
            print('可調整緋奈速度再次進行確認')
            print('請輸入攻擊數值')
            ATK = int(input())
            print('請輸入腕力數值')
            PWR = int(input())
            print('請輸入魔力數值')
            MATK = int(input())
            print('請輸入速度數值')
            SPD = int(input())
            BASE = (ATK-DEF/4)*(PWR/32+1)*3.25*(((10*MATK+16)**0.5-4)/64+1)
            k = len(p)
            while k != 1:
                print('請輸入傷害值')
                rDMG = int(input())
                for i in range(16,48):
                    for eSPD in p:
                        M = 0.01*math.floor(200*SPD/eSPD)
                        tDMG = math.floor(math.floor((BASE+ATK*i/25.6)*M)*RST)
                        if tDMG == rDMG:
                            d2.append(eSPD)
                p = d2
                d2 = []
                k = len(p)
            print('敵方的速度是'+str(p[0]))
input()