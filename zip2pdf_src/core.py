from pathlib import Path
import zipfile
import shutil
import img2pdf
from pprint import pprint
import click


@click.command()
@click.argument('zip_file', type=click.Path(exists=True))
@click.option('--log', '-l', is_flag=True, help="""Make Export_log.txt""")
def zip2pdf(zip_file, log):

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

    Foldername = Path(ZIP_FILE.stem)
    Foldername.mkdir()

    for image in image_list:
        pdf_path = Foldername / Path(Path(image).name).with_suffix('.pdf')
        try:
            with zipfilepointer.open(image) as img:
                with open(str(pdf_path), 'wb') as op:
                    op.write(img2pdf.convert(img))
                    op.close()
        except:
            print('Error:', image)
            zipfilepointer.extract(image, Foldername / 'Faild')
            Error_list.append(image)
        else:
            Sucsess_list.append(image)

    cleanup_Faild(Foldername)

    if log:
        export_log(zip_list, Sucsess_list, Error_list, Foldername)

    print('\nConvert Succeeded:')
    pprint(Sucsess_list)
    print('\nConvert Faild:')
    pprint(Error_list)


def cleanup_Faild(Foldername):
    folder = Path(Foldername / 'Faild')
    for p in folder.glob('**/*'):
        if p.is_file():
            p.replace(folder / p.name)

    for p in folder.glob('*'):
        if p.is_dir():
            shutil.rmtree(p)


def export_log(zip_list, Sucsess_list, Error_list, Foldername):
    with open(Foldername / 'Export_log.txt', 'w') as f:
        print('zip file list:', file=f)
        pprint(zip_list, stream=f)
        print('\nComvert Succeeded:', file=f)
        pprint(Sucsess_list, stream=f)
        print('\nConvert Faild:', file=f)
        pprint(Error_list, stream=f)
        f.close()
    print('\nLog output: Export_log.txt')


def main():
    zip2pdf()


if __name__ == '__main__':
    main()
