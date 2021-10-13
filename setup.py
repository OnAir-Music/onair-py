import setuptools
from importlib.machinery import SourceFileLoader


version = SourceFileLoader(
    'onair.version', 'onair/version.py'
).load_module()

with open('README.md', 'r') as fdesc:
    long_description = fdesc.read()


if __name__ == "__main__":
    setuptools.setup(
        # Name of the project
        name='onair',

        # Version
        version=version.version,

        # Description
        description='Python loader for the OnAir Music dataset',
        url='https://github.com/OnAir-Music/onair-py',

        # Your contact information
        author='Sevag Hanssian',
        author_email='sevag.hanssian+onair@gmail.com',

        # License
        license='MIT',

        # Packages in this project
        # find_packages() finds all these automatically for you
        packages=setuptools.find_packages(),

        long_description=long_description,
        long_description_content_type='text/markdown',

        # Dependencies, this installs the entire Python scientific
        # computations stack
        install_requires=[
            'numpy>=1.7',
            'stempeg>=0.2.3',
            'pyaml',
            'tqdm',
            'museval'
        ],

        zip_safe=False,
    )
