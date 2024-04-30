from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ve-gans",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    author="Zai",
    author_email="zaiyellyintaung@gmail.com",
    description="Floorplan generation model with pytorch",
    long_description="Detailed description of your project",
    url="https://github.com/zaibutcooler/ve-gans",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
