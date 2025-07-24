from setuptools import setup, find_packages

setup(
    name='dnatoolkit',
    version='0.1',
    description='A mini DNA sequence analysis library with CLI support',
    author='Sreeharsh K',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dnacli=dnacli:main'
        ]
    },
    install_requires=[],
)
