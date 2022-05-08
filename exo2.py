
import time
import requests
from threading import Thread

url = ["http://ftp.sra.ebi.ac.uk/vol1/fastq/SRR130/005/SRR13015805/SRR13015805_1.fastq.gz",
        "http://ftp.sra.ebi.ac.uk/vol1/fastq/SRR130/005/SRR13015805/SRR13015805_2.fastq.gz"]
file_name = ["fichier1","fichier2"]



def download(url):
    file_name = url.split("/")[-1]
    #response = requests.get(url)
    with open(file_name, "wb") as f:
        r = requests.get(url)
        f.write(r.content)
debut = int(time.time() * 10)

for i in range(2):
    t = Thread(target=download, args=(url[i],))
    t.start()

fin = int(time.time() * 10)
temps = fin - debut
print("Temps ecoule : ", temps)