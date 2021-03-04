import math
import time

print('請輸入我方防禦')
DEF = int(input())
d1 = []
d2 = []

print('請輸入傷害值')
rDMG = int(input())
if rDMG == 8:
    print('請輸入爆擊傷害')
    rDMG = int(input())
    start = time.time()
    PWRmin = math.ceil(DEF/4)
    for i in range(16,48):
        for PWR in range(PWRmin,1001):
            tDMG = math.floor((PWR-DEF/4)*(PWR/32+1)*3.25+PWR*i/25.6)
            if tDMG == rDMG:
                d1.append(PWR)
                break
            if tDMG > rDMG:
                break
    end = time.time()
    print('runtime',end-start,'sec')
else:
    start = time.time()
    for i in range(16,48):
        for PWR in range(0,1001):
            tDMG = math.floor((PWR-DEF/2)*(PWR/32+1)*1.75+PWR*i/25.6)
            if tDMG == rDMG:
                d1.append(PWR)
                break
            if tDMG > rDMG:
                break
    end = time.time()
    print('runtime',end-start,'sec')

k = len(d1)
while k != 0 and k != 1:
    print('請輸入傷害值')
    rDMG = int(input())
    if rDMG == 8:
        print('請輸入爆擊傷害')
        rDMG = int(input())
        start = time.time()
        for i in range(16,48):
            for PWR in d1:
                tDMG = math.floor((PWR-DEF/4)*(PWR/32+1)*3.25+PWR*i/25.6)
                if tDMG == rDMG:
                    d2.append(PWR)
        d1 = d2
        d2 = []
        k = len(d1)
        end = time.time()
        print('runtime',end-start,'sec')
    else:
        start = time.time()
        for i in range(16,48):
            for PWR in d1:
                tDMG = math.floor((PWR-DEF/2)*(PWR/32+1)*1.75+PWR*i/25.6)
                if tDMG == rDMG:
                    d2.append(PWR)
        d1 = d2
        d2 = []
        k = len(d1)
        end = time.time()
        print('runtime',end-start,'sec')
if k == 0:
    print('error...')
elif k == 1:
    print('敵方的腕力是',d1[0])