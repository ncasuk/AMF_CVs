from setuptools import setup

VERSION = "2.0.0"

setup(
    name="AMF_CVs",
    author="Ag Stephens",
    author_email="ag.stephens@stfc.ac.uk",
    url="https://github.com/ncasuk/AMF_CVs",
    version=VERSION,
    description="AMF controlled vocabularies",
    data_files=[
        ('': ['AMF_CVs/*', 'product-definitions/*', 'pyessv-vocabs/*'])
    ],
    include_package_data=True
)
