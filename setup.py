from setuptools import setup,find_packages #find_packages har folder me ghuske dekhta hai if there is init.py to covert that folder to a package.

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.2",
    author="Mokshtrial1",
    packages=find_packages(),
    install_requires = requirements,
)