import math
import time

print('請選擇計算模式(正常:1,弱點:2,耐性:3,吸收:4)')
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
elif mode == 4:
    RST = 0.5

d1 = []
d2 = []

print('請輸入傷害值')
rDMG = int(input())
if rDMG == 0:
    print('請輸入無爆擊傷害值')
    rDMG = int(input())
    start = time.time()
    BASE = (ATK-DEF/2)*(PWR/32+1)*1.75*(((10*MATK+16)**0.5-4)/64+1)
else:
    start = time.time()
    BASE = (ATK-DEF/4)*(PWR/32+1)*3.25*(((10*MATK+16)**0.5-4)/64+1)
print('-----')
for i in range(16,48):
    for M in range(200,1001):
        tDMG = math.floor(math.floor((BASE+ATK*i/25.6)*0.01*M)*RST)
        if tDMG == rDMG:
            d1.append(M)
            print(M)
        if tDMG > rDMG:
            break
print('-----')
end = time.time()
#print('runtime',end-start,'sec')
k = len(d1)

while k != 0 and k != 1:
    print('請輸入傷害值')
    rDMG = int(input())
    if rDMG == 0:
        print('請輸入無爆擊傷害值')
        rDMG = int(input())
        start = time.time()
        BASE = (ATK-DEF/2)*(PWR/32+1)*1.75*(((10*MATK+16)**0.5-4)/64+1)
    else:
        start = time.time()
        BASE = (ATK-DEF/4)*(PWR/32+1)*3.25*(((10*MATK+16)**0.5-4)/64+1)
    print('-----')
    for i in range(16,48):
        for M in d1:
            tDMG = math.floor(math.floor((BASE+ATK*i/25.6)*0.01*M)*RST)
            if tDMG == rDMG:
                d2.append(M)
                print(M)
    d1 = d2
    d2 = []
    k = len(d1)
    print('-----')
    end = time.time()
    #print('runtime',end-start,'sec')

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
        start = time.time()
        for eSPD in range(math.ceil(SPD/5),SPD+1):
            if math.floor(200*SPD/eSPD) == M:
                p.append(eSPD)
            if math.floor(200*SPD/eSPD) < M:
                break
        end = time.time()
        #print('runtime',end-start,'sec')
        if len(p) == 1:
            print('敵方的速度是',p[0])
        elif len(p) == 0:
            print('error...')
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
            k = len(p)
            while k != 1:
                print('請輸入傷害值')
                rDMG = int(input())
                if rDMG == 0:
                    print('請輸入無爆擊傷害值')
                    rDMG = int(input())
                    start = time.time()
                    BASE = (ATK-DEF/2)*(PWR/32+1)*1.75*(((10*MATK+16)**0.5-4)/64+1)
                else:
                    start = time.time()
                    BASE = (ATK-DEF/4)*(PWR/32+1)*3.25*(((10*MATK+16)**0.5-4)/64+1)
                for i in range(16,48):
                    for eSPD in p:
                        M = 0.01*math.floor(200*SPD/eSPD)
                        tDMG = math.floor(math.floor(math.floor((BASE+ATK*i/25.6)*M)*RST)*1.5)
                        if tDMG == rDMG:
                            d2.append(eSPD)
                p = d2
                d2 = []
                k = len(p)
                end = time.time()
                print('runtime',end-start,'sec')
            print('敵方的速度是',p[0])