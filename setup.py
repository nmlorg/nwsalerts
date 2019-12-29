import setuptools


setuptools.setup(
    name='nwsalerts',
    version='0.0.1',
    author='Daniel Reed',
    author_email='nmlorg@gmail.com',
    url='https://github.com/nmlorg/nwsalerts',
    packages=setuptools.find_packages(include=('nwsalerts', 'nwsalerts.*')),
    python_requires='>=3.5',
    install_requires=[
        'requests',
    ])
