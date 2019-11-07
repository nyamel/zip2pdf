from pathlib import Path
import zipfile
import pprint
import img2pdf


ZIP_FILE = Path(r'./test-20191103T160942Z-001.zip')

zipfilepointer = zipfile.ZipFile(ZIP_FILE)

# print(len(zipfilepointer.namelist())) 項目数獲得成功

zip_list = zipfilepointer.namelist()
# pprint.pprint(file_list)

path_list = [Path(f'./{i}') for i in zip_list]

ex_li = ['.jpg', '.jpeg', '.jpe', '.jfif', '.png', '.gif',
         '.tif', '.tiff', '.nsk', '.bmp', '.dib', '.rle']
EX_li = list(map(lambda x: x.upper(), ex_li))
# print(EX_li)

Extends = set(ex_li + EX_li)

image_list = [str(p) for p in path_list if p.suffix in Extends]

Sucsess_list = []
Error_list = []

Filename = Path(ZIP_FILE.stem)
Filename.mkdir()

i = 0
for image in image_list:
    try:
        with zipfilepointer.open(image) as img:
<<<<<<< HEAD
            with open(str(Filename / Path(Path(image).name).with_suffix('.pdf')), 'wb') as op:
=======
            with open(str(Filename/Path(Path(image).name).with_suffix('.pdf')),'wb') as op:
>>>>>>> 50a9bf2bd984733fc0297fe4b756c4b00237fc18
                op.write(img2pdf.convert(img))
                op.close()
    except:
        print('Error:', image)
<<<<<<< HEAD
        zipfilepointer.extract(image, Filename / 'Faild')
=======
        zipfilepointer.extract(image, Filename/'Faild')
>>>>>>> 50a9bf2bd984733fc0297fe4b756c4b00237fc18
        Error_list.append(image)
    else:
        print('Sucsess:', image)
        Sucsess_list.append(image)
        i += 1


print('\nConvert Sucsess:')
pprint.pprint(Sucsess_list)
print('\nConvert Faild:')
pprint.pprint(Error_list)

# alpha channelの警告文: img2pdf ソース 1038行目付近
