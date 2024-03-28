from setuptools import setup, find_packages

setup(
    name='concat-files-py',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'concat-files=concat_files_py.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A utility to concatenate file contents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/concat-files-py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)