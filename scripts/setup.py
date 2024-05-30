from setuptools import setup

setup(
    name='virtbc',
    version='0.1.3',
    entry_points={
        'console_scripts': [
            'virtbc = virtbc:main',
        ],
    },
)
