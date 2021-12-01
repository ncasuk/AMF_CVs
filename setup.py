from setuptools import setup

VERSION = "2.0.0"

setup(
    name="AMF_CVs",
    version=VERSION,
    description="AMF controlled vocabularies",
    package_data={'': ['AMF_CVs', 'product-definitions', 'pyessv-vocabs']},
    include_package_data=True
)
