from setuptools import setup, find_packages

setup(
    name='database-tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'redshift_connector',
        'pandas',
    ],
)
