from setuptools import setup, find_packages

setup(
    name='tlrrt_star',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.12.3',
        'matplotlib==3.8.3',
        'networkx==3.2.1',
        'numpy==1.26.4',
        'pyvisgraph==0.2.1',
        'Requests==2.31.0',
        'scipy==1.13.0',
        'Shapely==2.0.3',
        'sympy==1.12',
        'termcolor==2.4.0',
    ],
    author='Xusheng Luo',
    author_email='xusheng.luo2@gmail.com',
    description='Cource code for the paper "An Abstraction-Free Method for Multirobot Temporal Logic Optimal Control Synthesis"',
    license='MIT',
    url='https://github.com/XushengLuo92/TLRRT_star',
)
