from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ve-gans',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            've-gans-train=ve_gans.train:main',
            've-gans-generate=ve_gans.generate:main',
        ],
    },
    author='Zai',
    author_email='zaiyellyintaung@gmail.com',
    description='Image generation with GANs using PyTorch',
    long_description='Detailed description of your project',
    url='https://github.com/zaibutcooler/ve-gans',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
