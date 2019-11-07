import os
from pathlib import Path
import zipfile
import shutil
from pprint import pprint
import img2pdf

folder = Path('test-20191103T160942Z-001/Faild')

pprint(list(folder.glob('**/*')))

i = 0
for p in folder.glob('**/*'):
    if p.is_file():
<<<<<<< HEAD
        p.replace(folder / p.name)
=======
        p.replace(folder/p.name)
>>>>>>> 50a9bf2bd984733fc0297fe4b756c4b00237fc18
        i += 1


for p in folder.glob('*'):
    if p.is_dir():
        shutil.rmtree(p)
