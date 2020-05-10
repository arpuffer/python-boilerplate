from setuptools import setup, find_packages
PKG = "Pkg"  # These are defined in multiple places--could use a tool such as versioneer or setuptools scm to auto version
VERSION = "Ver" # https://packaging.python.org/guides/distributing-packages-using-setuptools/#scripts

setup(
    name=PKG,
    version=VERSION,
    author="Name",
    description="Descr",
    packages=find_packages(),
    provides=[PKG],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
    """ For executable CLI scripts w/out 'python -m myscript' see the following from
    https://packaging.python.org/guides/distributing-packages-using-setuptools/#scripts and
    https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation : 

    entry_points={
    "console_scripts": [
        "foo = my_package.some_module:main_func",
        "bar = other_module:some_func",
        ],
    "gui_scripts": [
        "baz = my_package_gui:start_func",
        ]
    }

    """ 
)
