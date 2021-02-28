import math

DEF = 69
MATK = 0
INT = 0
MATK = 0
skillmul = 0
d1 = []
d2 = []
d3 = []
fDMG = 10807
DMG = [10824,10841,10858,10875,10892,10909,10943,10960,11011,11028,11045,11062,11079,11096,11113,11130,11147,11164,
11181,11198,11215,11232,11249,11266,11283,11300,11317,11334,11368,11385,11402,11436,11453,11487,11504,11521,11555,
11572,11589,11623,11640,11657,11674,11691,11708,11742,11810,11827,11844,11861]

for INT in range(1,1001):
    MOD = ((INT*10+16)**0.5-4)/64+1
    for MATK in range(INT,1001):
        for skillmul in range(1,10001):
            for i in range(32,95):
                tDMG = math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul*0.01)
                if tDMG == fDMG:
                    match = [MATK,INT,skillmul]
                    d1.append(match)
print('.')

for rDMG in DMG:
    for match in d1:
        MATK = match[0]
        INT = match[1]
        skillmul = match[2]
        MOD = ((INT*10+16)**0.5-4)/64+1
        for i in range(32,95):
            tDMG = math.floor(((MATK-DEF/2)*(INT/32+1)*1.75*MOD+MATK*i/25.6)*skillmul*0.01)
            if tDMG == rDMG:
                match2 = [MATK,INT,skillmul]
                d2.append(match2)
    d1 = d2
    d2 = []
    print('.')

print('results:')
for match in d1:
    print('MATK = '+str(match[0]))
    print('INT = '+str(match[1]))
    print('skillmul = '+str(match[2])+'%')
print('over')
input()