import os
from pathlib import Path
import zipfile
import img2pdf
from pprint import pprint
import click


@click.command()
@click.argument('zip_file', type=click.Path(exists=True))
@click.option('--log', '-l', is_flag=True, help="""Make Export_log.txt""")
def cmd(zip_file, log):

    ZIP_FILE = Path(zip_file)
    zipfilepointer = zipfile.ZipFile(ZIP_FILE)

    zip_list = zipfilepointer.namelist()
    path_list = [Path(f'./{i}') for i in zip_list]

    ex_li = ['.jpg', '.jpeg', '.jpe', '.jfif', '.png', '.gif',
             '.tif', '.tiff', '.nsk', '.bmp', '.dib', '.rle']
    EX_li = list(map(lambda x: x.upper(), ex_li))
    Extends = set(ex_li + EX_li)

    image_list = [str(p) for p in path_list if p.suffix in Extends]

    Sucsess_list = []
    Error_list = []

    Filename = ZIP_FILE.stem
    os.mkdir(Filename)

    i = 0
    for image in image_list:
        try:
            with zipfilepointer.open(image) as img:
                with open(f'{Filename}/image{i}.pdf', 'wb') as op:
                    op.write(img2pdf.convert(img))
                    op.close()
        except:
            print('Error:', image)
            zipfilepointer.extract(image, Filename + '/Faild')
            Error_list.append(image)
        else:
            Sucsess_list.append(image)
            i += 1

    if log:
        export_log(zip_list, Sucsess_list, Error_list, Filename)

    print('\nConvert Succeeded:')
    pprint(Sucsess_list)
    print('\nConvert Faild:')
    pprint(Error_list)


def export_log(zip_list, Sucsess_list, Error_list, Filename):
    with open(Filename + '/Export_log.txt', 'w') as f:
        print('zip file list:', file=f)
        pprint(zip_list, stream=f)
        print('\nComvert Succeeded:', file=f)
        pprint(Sucsess_list, stream=f)
        print('\nConvert Faild:', file=f)
        pprint(Error_list, stream=f)
        f.close()
    print('\nLog output: Export_log.txt')


def main():
    cmd()


if __name__ == '__main__':
    main()
