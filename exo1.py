import numpy as np
import time
import statistics

debut = int(time.time()*10)
np.random.RandomState(1000000)
nbr = np.random.randint(0,10, size=1000000)
data = nbr.tolist()
element = len(data)
data[:1000000]

moyenne= statistics.mean(data)
fin = int(time.time()*10)
temps = fin-debut
print("le nombre d'élément est :", element)
print(moyenne)
print("Temps ecoule : ",temps)