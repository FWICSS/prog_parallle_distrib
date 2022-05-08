import random
import time
import statistics
from joblib import Parallel, delayed


def calculM(data):
    calcul = statistics.mean(data)
    return calcul


print('Entrez le nombre de coeur a utilisez  (4 maximum)')
nbcoeur = int(input())

if (0 < nbcoeur < 5):
    debut = int(time.time() * 10)
    data = []
    data.append(random.randint(0, 1000000))
    nbrelement = len(data)
    moyenne = calculM(data)
    fin = int(time.time() * 10)
    temps = fin - debut
    print(moyenne)
    print("Temps ecoule : ", temps)
else:
    print("le nombre saisie n'est pas compris entre 0 et 4")
    nbcoeur = input()

Parallel(n_jobs=nbcoeur)(delayed(calculM(data)) for i in range(nbrelement))