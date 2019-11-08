from setuptools import setup, find_packages

setup(
    name='zip2pdf',
    version='0.2.2',
    author='nyamel',
    author_email='twilight6sachirin@gmail.com',
    url='https://github.com/nyamel/zip2pdf',
    licence='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'img2pdf',
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'zip2pdf=zip2pdf.core:main'
        ]
    }
)
