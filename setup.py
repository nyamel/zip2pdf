from setuptools import setup

setup(
    name='zip2pdf',
    version='0.1',
    author='nyamel',
    author_email='twilight6sachirin@gmail.com',
    url='https://github.com/nyamel/zip2pdf',
    licence='MIT',
    install_requires=[
        'img2pdf',
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'zip2pdf=zip2pdf_src.core:main'
        ]
    }
)
