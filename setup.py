from setuptools import setup, find_packages

setup(
    name='MYPACKAGE',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url="https://github.com/Gathage-2023/Gathage-2023.git/<myModule.py>",
    author='Joseph Gathage',
    author_email='josegathage2013@gmail.com'
)
