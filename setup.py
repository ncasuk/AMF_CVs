from setuptools import setup
import os

VERSION = "2.0.0"


def collect_files(*dirs):
    "Walks file tree to return a list of all file paths under each dir in dirs."
    file_paths = []

    for dr in dirs:
        for d, _2, paths in os.walk(dr):
            for fname in paths:
                fpath = os.path.join(d, fname)
                file_paths.append(fpath)

    return file_paths


setup(
    name="AMF_CVs",
    author="Ag Stephens",
    author_email="ag.stephens@stfc.ac.uk",
    url="https://github.com/ncasuk/AMF_CVs",
    version=VERSION,
    description="AMF controlled vocabularies",
    packages=["test_setup"],
#    package_data={'test_setup': ['test_setup/hello.world']},
    data_files=[('', collect_files('test_setup'))],
#    data_files=[
#        ('AMF_CVs', collect_files('AMF_CVs', 'product-definitions', 'pyessv-vocabs'))
#    ],
    include_package_data=True
)
