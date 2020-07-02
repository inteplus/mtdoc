Installation
============

Minh-Tri Pham's Python namespace packages use the following convention. If the package name in Python is `mt.xyz` then its corresponding name in pypi.org is `mtxyz`. This is because pypi does not yet support namespace packages, as of 2020/06/01. Currently, the packages are: `mt.base`, `mt.pandas`, `mt.struct`, `mt.geo`, `mt.sql`, `mt.skimage` and `mt.opencv`.

In the following instructions, replace `xyz` with the package name of your choosing.

Install via pip::

    pip3 install mtxyz

Build from source::

    git clone https://github.com/inteplus/mtxyz.git
    cd mtxyz
    python3 setup.py install

mt.struct
---------

If the package `mt.xyz` is `mt.struct` then the Python source code is located at subfolder `python` instead. Apart from the Python source code, `mt.struct` contains C++ source code, which can be built into a C++ library using th following instructions.

Use cmake to build and install::

    git clone https://github.com/inteplus/mtstruct.git
    cd mtstruct/cpp
    mkdir build
    cd build
    cmake ..
    make
    make install
