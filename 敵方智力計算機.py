import math
import time

print('請輸入我方魔防')
MDEF = int(input())
print('請輸入敵方技能屬性(有屬:1,無屬:2)')
element = int(input())
INTmin = math.ceil(MDEF/2)
match1 = []
match2 = []
Base = []
INTlist = range(INTmin,1001)
if element == 1:
    for INT in INTlist:
        Base.append((INT-MDEF/2)*(INT/32+1)*1.75*(((INT*10+16)**0.5-4)/64+1))
else:
    for INt in INTlist:
        Base.append((INT-MDEF/2)*(INT/32+1)*1.75)

print('請輸入傷害值')
rDMG = int(input())
start = time.time()
for i in range(0,1001-INTmin):
    for j in range(32,95):
        maxguess = math.ceil(rDMG/int(Base[i]+INTlist[i]*j/25.6)*10)
        minguess = math.floor(rDMG/int(Base[i]+INTlist[i]*j/25.6)*10)
        for skillmul in range(minguess,maxguess+1):
            tDMG = int((Base[i]+INTlist[i]*j/25.6)*skillmul*0.1)
            if tDMG == rDMG:
                match1.append([Base[i],INTlist[i],skillmul])
                #print(Base[i],INTlist[i],skillmul)
                break
            elif tDMG > rDMG:
                break
end = time.time()
print('runtime',end-start,'sec')

k = len(match1)
while k != 1 and k != 0:
    print('請輸入傷害值')
    rDMG = int(input())
    start = time.time()
    for match in match1:
        for j in range(32,95):
          tDMG = int((match[0]+match[1]*j/25.6)*match[2]*0.1)
          if tDMG == rDMG:
            match2.append([match[0],match[1],match[2]])
            #print(match[0],match[1],match[2])
    match1 = match2
    match2 = []
    end = time.time()
    k = len(match1)
    print('runtime',end-start,'sec')

if k == 0:
  print('error')
elif k == 1:
  print('敵方的智力是',match1[0][1])
  print('敵方的技能倍率是',match1[0][2]*10,'%')