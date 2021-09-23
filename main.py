import os
import zipfile
from clint.textui import progress

import requests

cleomodreq = "http://cleo.li/cleo4/CLEO4.zip"
cleoreq = requests.get(cleomodreq)

print("Downloading CLEO4...")

with open(r"./CLEO4.zip", "wb") as zip:
    total_length = int(cleoreq.headers.get('content-length'))
    for chunk in progress.bar(cleoreq.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
        if chunk:
            zip.write(chunk)
            zip.flush()

print("Download Complete!")
print("Extracting zip file...")

with zipfile.ZipFile(r"./CLEO4.zip", "r") as zip_ref:
    zip_ref.extractall()

print("Extracting Done!")

os.remove(r"./CLEO4.zip")

silentasireq = "https://www.gtagarage.com/mods/download.php?f=37262"
silentreq = requests.get(silentasireq)

print("Downloading Silent ASI Loader 13...")

with open(r"./silents_asi_loader_13.zip", "wb") as zip1:
    total_length = int(silentreq.headers.get('content-length'))
    for chunk in progress.bar(silentreq.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
        if chunk:
            zip1.write(chunk)
            zip1.flush()

print("Download Complete!")
print("Extracting zip file...")

with zipfile.ZipFile(r"./silents_asi_loader_13.zip", "r") as zip_ref1:
    zip_ref1.extractall()

print("Extracting Done!")

os.remove(r"./silents_asi_loader_13.zip")

print("All ZIP Files are auto deleted!")

os.system("pause")