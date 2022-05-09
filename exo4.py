import time
import random
from numpy import zeros
from threading import Thread
N = 100
tab = zeros(100,int)

def t1(tab):
    for i in range(1,100):
        tab[i] = (tableau[i1] + tableau[i] + tableau[i + 1]) / 3
    return tab


def t2(tab):
    print(tab)
    time.sleep(4)


def main():
    for i in range (1,100):
        if i == 0 or i == 99:
            tab[i]=0
        else :
            tab[i]=random.randint(0,100)

    T1 = Thread(target=t1, args=(tab))
    T2 = Thread(target=t2, args=(tab))
    T1.start() and T2.start()

main()