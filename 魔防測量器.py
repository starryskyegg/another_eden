import math
import time

print('請選擇計算模式(正常:1,弱點:2,耐性:3,吸收:4)')
mode = int(input())
if mode == 1:
    RST = 1
elif mode == 2:
    RST = 2
elif mode == 3:
    RST = 0.25
elif mode == 4:
    RST = 0.5

print('請選擇屬性有無(有屬性:1,無屬性:2)')
element = int(input())

print('請輸入技能倍率')
skillmul = float(input())

print('請輸入魔力數值')
MATK = int(input())

print('請輸入知性數值')
INT = int(input())

if element == 1:
    MOD = ((INT*10+16)**0.5-4)/64+1
elif element == 2:
    MOD = 1

DEF = 0
d1 = []
d2 = []

print('請輸入傷害值')
rDMG = int(input())
if rDMG == 8:
    print('請輸入爆擊傷害')
    rDMG = int(input())
    start = time.time()
    for i in range(32,95):
        while DEF <= MATK*2:
            tDMG = math.floor(math.floor(((MATK-DEF/4)*(INT/32+1)*3.25*MOD+MATK*i/25.6)*skillmul)*RST)
            if tDMG == rDMG:
                d1.append(DEF)
                break
            DEF+=1
            if tDMG < rDMG:
                break
        DEF = 0
    end = time.time()
    #print('runtime',end-start,'sec')
else:
    start = time.time()
    for i in range(32,95):
        while DEF <= MATK*2:
            tDMG = math.floor(math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)*RST)
            if tDMG == rDMG:
                d1.append(DEF)
                break
            DEF+=1
            if tDMG < rDMG:
                break
        DEF = 0
    end = time.time()
    #print('runtime',end-start,'sec')

k = len(d1)
while k != 0 and k != 1:
    print('請輸入傷害值')
    rDMG = int(input())
    if rDMG == 8:
        print('請輸入爆擊傷害')
        rDMG = int(input())
        start = time.time()
        for i in range(32,95):
            for DEF in d1:
                tDMG = math.floor(math.floor(((MATK-DEF/4)*(INT/32+1)*3.25*MOD+MATK*i/25.6)*skillmul)*RST)
                if tDMG == rDMG:
                    d2.append(DEF)
        d1 = d2
        d2 = []
        k = len(d1)
        end = time.time()
        #print('runtime',end-start,'sec')
    else:
        start = time.time()
        for i in range(32,95):
            for DEF in d1:
                tDMG = math.floor(math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)*RST)
                if tDMG == rDMG:
                    d2.append(DEF)
        d1 = d2
        d2 = []
        k = len(d1)
        end = time.time()
        #print('runtime',end-start,'sec')
if k == 0:
    print('error...')
elif k == 1:
    print('敵方的魔防是',d1[0])