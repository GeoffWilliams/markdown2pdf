import os
from setuptools import setup


def gen_data_files(*dirs):
    results = []

    for src_dir in dirs:
        for root,dirs,files in os.walk(src_dir):
            results.append((root, map(lambda f:root + "/" + f, files)))
    return results

def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()


setup(
    name='Markdown2PDF',
    version='0.1.3',
    url='https://github.com/kxxoling/markdown2pdf',
    license='MIT',
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    description='A tool converts Markdown file to PDF, '
                'originally designed for developers\' resume release.',
    long_description=fread('README.rst'),
    packages=['markdown2pdf'],
    zip_safe=False,
    platforms='any',
    data_files=gen_data_files("markdown2pdf/themes")
    install_requires=[
        'weasyprint',
        'misaka',
    ],
    entry_points={
        'console_scripts': [
            'md2pdf = markdown2pdf:main',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
