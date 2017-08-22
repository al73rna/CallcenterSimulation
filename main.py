import random as rnd
from queue import *
customers = 100
worldTime = -1
AbleService = 1
BakerService = 1
ArrivalTime = 1
D = []
Q = []

def ATgen():
    tmp = rnd.randrange(0,100)
    if 0<=tmp<25 :
        return 1
    if 25<=tmp<65 :
        return 2
    if 65<=tmp<85 :
        return 3
    if 85<=tmp<=100 :
        return 4
def ABLgen():
    tmp = rnd.randrange(0,100)
    if 0<=tmp<30 :
        return 2
    if 30<=tmp<58 :
        return 3
    if 58<=tmp<83 :
        return 4
    if 83<=tmp<=100 :
        return 5

def BAKgen():
    tmp = rnd.randrange(0,100)
    if 0<=tmp<35 :
        return 3
    if 35<=tmp<60 :
        return 4
    if 60<=tmp<80 :
        return 5
    if 80<=tmp<=100 :
        return 6



while(True) :



    worldTime += 1
    ArrivalTime -= 1
    if AbleService != 0:
        AbleService -= 1
    if BakerService != 0 :
        BakerService -= 1

    if len(Q) != 0:
        for i in range(len(Q)):
            Q[i]= Q[i]+1

    if(len(D) == 1000):
        break
    if ArrivalTime == 0 :
        Q.append(0)

    print(D,Q,ArrivalTime,AbleService,BakerService)


    if AbleService == 0 :
        if(len(Q)!=0):
            D.append(Q.pop(0))
            AbleService = ABLgen()


    if AbleService != 0 and BakerService == 0 :
        if(len(Q)!=0):
            D.append(Q.pop(0))

        BakerService = BAKgen()



    if ArrivalTime == 0 :
        ArrivalTime = ATgen()

    print(D,Q,"+>++",AbleService,BakerService)
    #if worldTime == 20:
     #   break



num0=0
num1=0
num2=0
num3=0
num4=0
num5=0
p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in D :
    p[i]+=1

print(p,len(D))