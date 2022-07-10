from Bio import Entrez
Entrez.email = "senuri.piyatissa@gmail.com"

# To obtain the list of databases
handle = Entrez.einfo()
rec = Entrez.read(handle)
handle.close()
print(rec.keys())
print(rec['DbList'])