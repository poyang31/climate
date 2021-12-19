from setuptools import setup

with open('requirements.txt') as fid:
    requires = [line.strip() for line in fid]

setup(
    name='climate',
    version='1.0.0',
    packages=[''],
    url='https://github.com/poyang31/hw_2021_12',
    license='MIT License',
    author='Po-Yang Chen',
    author_email='poyang31@yahoo.com.tw',
    description='The analyzer for Internet trends in Taiwan.',
    install_requires=requires
)
