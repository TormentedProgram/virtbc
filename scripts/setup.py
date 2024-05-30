from setuptools import setup

setup(
    name='virtbc',
    version='0.1.2',
    entry_points={
        'console_scripts': [
            'virtbc = virtbc:main',
        ],
    },
)
