import time
import random
from threading import Thread

#debut = int(time.time()*10)
tab = []
'''
for line in tab:
    print(line)
'''

def Moyenne(i):
    print("\n Début calcule colonne %d\n" %i)
    somme = 0
    for line in range(0,99):
        somme = somme + tab[line][i]
    moyenne=somme/100
    print("la moyenne de la colonne %d est de :" %i ,moyenne,end="\n")

for line in range(0, 99):
    nvline = []
    for col in range(0, 99):
        value = random.randint(1, 90)
        nvline.append(value)
    tab.append(nvline)

def main():
    for i in range(0,99):
        t = Thread(target=Moyenne, args=(i,))
        t.start()

if __name__ == '__main__':
    main()