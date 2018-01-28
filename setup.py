from setuptools import setup

setup(
    name='tetris',
    version='0.1.0',
    packages=['tetris'],
    entry_points={
        'console_scripts': [
            'tetris = tetris.__main__:main'
        ]
    })
