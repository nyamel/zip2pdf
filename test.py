# 画像だけ解凍
from pathlib import Path
import zipfile
import pprint

ZIP_FILE = './test-20191103T160942Z-001.zip'

zipfilepointer = zipfile.ZipFile(ZIP_FILE)

# print(len(zipfilepointer.namelist())) 項目数獲得成功！

zip_list = zipfilepointer.namelist()

# pprint.pprint(file_list)

path_list = [Path(f'./{i}') for i in zip_list]

ex_li = ['.jpg', '.jpeg', '.jpe', '.jfif', '.png', '.gif',
               '.pdf', '.tif', '.tiff', '.nsk', '.bmp', '.dib', '.rle']
EX_li = list(map(lambda x: x.upper(), ex_li))
# print(EX_li)

Extends = set(ex_li + EX_li)

image_list = [p for p in path_list if p.suffix in Extends]

for image in image_list:
    zipfilepointer.extract(str(image), './test1')
