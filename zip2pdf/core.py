from pathlib import Path
import zipfile
import shutil
import img2pdf
from pprint import pprint
import click


@click.command()
@click.argument('zip_file', type=click.Path(exists=True))
@click.option('--rename', '-r', type=click.Path(), help="Rename output derectry")
@click.option('--log', '-l', is_flag=True, help="Make Export_log.txt")
def zip2pdf(zip_file, log, rename):
    """Convert images in zipfile to pdf."""

    ZIP_FILE = Path(zip_file)
    zipfilepointer = zipfile.ZipFile(ZIP_FILE)

    zip_list = zipfilepointer.namelist()
    path_list = [Path(fr'./{i}') for i in zip_list]

    ex_li = ['.jpg', '.jpeg', '.jpe', '.jfif', '.png', '.gif',
             '.tif', '.tiff', '.nsk', '.bmp', '.dib', '.rle']
    EX_li = list(map(lambda x: x.upper(), ex_li))
    Extends = set(ex_li + EX_li)

    image_list = [str(p) for p in path_list if p.suffix in Extends]

    Sucsess_list = []
    Error_list = []

    if rename:
        dirname = ZIP_FILE.parent / Path(rename)
    else:
        dirname = ZIP_FILE.parent / Path(ZIP_FILE.stem)
    dirname.mkdir()

    for image in image_list:
        pdf_path = dirname / Path(Path(image).name).with_suffix('.pdf')
        image = image.replace('¥¥', '/')
        try:
            with zipfilepointer.open(image) as img:
                with open(str(pdf_path), 'wb') as op:
                    op.write(img2pdf.convert(img))
                    op.close()
        except:
            print('Error:', image)
            zipfilepointer.extract(image, dirname / 'Faild')
            Error_list.append(image)
        else:
            Sucsess_list.append(image)

    cleanup_Faild(dirname)

    if log:
        export_log(zip_list, Sucsess_list, Error_list, dirname)

    print('\nConvert Succeeded:')
    pprint(Sucsess_list)
    print('\nConvert Faild:')
    pprint(Error_list)


def cleanup_Faild(dirname):
    folder = Path(dirname / 'Faild')
    for p in folder.glob('**/*'):
        if p.is_file():
            p.replace(folder / p.name)

    for p in folder.glob('*'):
        if p.is_dir():
            shutil.rmtree(p)


def export_log(zip_list, Sucsess_list, Error_list, dirname):
    with open(dirname / 'Export_log.txt', 'w') as f:
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
