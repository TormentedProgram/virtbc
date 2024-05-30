from setuptools import setup
import os

def find_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), directory))
    return files

setup(
    name='virtbc',
    version='0.1.1',
    entry_points={
        'console_scripts': [
            'virtbc = virtbc:main',
        ],
    },
    package_data={
        'virtbc': find_files(os.path.join(os.path.expanduser("~"), '.config', 'virtbc')),
    },
)
