import random
import time
from threading import Thread


compt = 20
compt1 = 0
compt2 = compt

def c1(compt1):
    while (compt1 < 100):
        compt1 += 1
        delais = random.randint(1,8)
        time.sleep(delais)
        print(compt1)


def c2(compt2):
    while (compt2 <= 100):
        compt2 += 1
        time.sleep(3)
        print(compt2)

t1 = Thread(target=c2(compt2))
t2 = Thread(target=c1(compt1))
for i in range(1,2):
        if i==1 :
            t1.start()
        else :
            t2.start()