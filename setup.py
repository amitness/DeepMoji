from setuptools import setup

setup(
    name='deepmoji',
    version='1.1',
    packages=['deepmoji'],
    description='DeepMoji library',
    include_package_data=True,
    install_requires=[
        'emoji==0.4.5',
        'numpy',
        'scikit-learn',
        'text-unidecode',
    ],
)
