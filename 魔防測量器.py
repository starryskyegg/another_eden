import math

print('請選擇計算模式(正常:1,弱點:2,耐性:3)')
mode = int(input())

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
d3 = []

if mode == 1:
    print('請輸入傷害值')
    rDMG = int(input())
    for i in range(32,95):
        while DEF <= MATK*2:
            tDMG = math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)
            if tDMG == rDMG:
                d1.append(DEF)
            DEF+=1
        DEF = 0
    k = len(d1)
    while k != 1:
        j = 0
        print('請輸入傷害值')
        rDMG = int(input())
        for i in range(32,95):
            while DEF <= MATK*2:
                tDMG = math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)
                if tDMG == rDMG:
                    d2.append(DEF)
                DEF+=1
            DEF = 0
        while j < len(d1):
            if d1[j] in d2 :
                d3.append(d1[j])
            j+=1
        d1 = d3
        d2 = []
        d3 = []
        k = len(d1)
    print('敵方的魔防是'+str(d1[0]))
elif mode == 2:
    print('請輸入傷害值')
    rDMG = int(input())
    for i in range(32,95):
        while DEF <= MATK*2:
            tDMG = math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)*2
            if tDMG == rDMG:
                d1.append(DEF)
            DEF+=1
        DEF = 0

    k = len(d1)
    while k != 1:
        j = 0
        print('請輸入傷害值')
        rDMG = int(input())
        for i in range(32,95):
            while DEF <= MATK*2:
                tDMG = math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)*2
                if tDMG == rDMG:
                    d2.append(DEF)
                DEF+=1
            DEF = 0
        while j < len(d1):
            if d1[j] in d2 :
                d3.append(d1[j])
            j+=1
        d1 = d3
        d2 = []
        d3 = []
        k = len(d1)
    print('敵方的魔防是'+str(d1[0]))
elif mode == 3:
    print('請輸入傷害值')
    rDMG = int(input())
    for i in range(32,95):
        while DEF <= MATK*2:
            tDMG = math.floor(math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)*0.25)
            if tDMG == rDMG:
                d1.append(DEF)
            DEF+=1
        DEF = 0

    k = len(d1)
    while k != 1:
        j = 0
        print('請輸入傷害值')
        rDMG = int(input())
        for i in range(32,95):
            while DEF <= MATK*2:
                tDMG = math.floor(math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul)*0.25)
                if tDMG == rDMG:
                    d2.append(DEF)
                DEF+=1
            DEF = 0
        while j < len(d1):
            if d1[j] in d2 :
                d3.append(d1[j])
            j+=1
        d1 = d3
        d2 = []
        d3 = []
        k = len(d1)
    print('敵方的魔防是'+str(d1[0]))
input()