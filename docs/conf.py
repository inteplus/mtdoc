# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "mt"
copyright = "2020, Minh-Tri Pham"
author = "Minh-Tri Pham"

# The full version, including alpha/beta/rc tags
release = "latest"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.napoleon",
    "autoapi.sphinx",
]

# autoapi
autoapi_modules = {
    "mt.aio": None,
    "mt.base": None,
    "mt.ctx": None,
    "mt.logg": None,
    "mt.concurrency": None,
    "mt.mpl": None,
    "mt.np": None,
    "mt.path": None,
    "mt.plt": None,
    "mt.shutil": None,
    "mt.threading": None,
    "mt.time": None,
    "mt.traceback": None,
    "mt.net": None,
    "mt.gpu": None,
    "mt.pandas": None,
    "mt.pd": None,
    "mt.tf": None,
    "mt.tfg": None,
    "mt.geo": {"template": "mt.geo"},
    "mt.geo2d": {"template": "mt.geo"},
    "mt.geo3d": {"template": "mt.geo"},
    "mt.geond": {"template": "mt.geo"},
    "mt.sql": None,
    "mt.skimage": None,
    "mt.cv": None,
    "mt.opencv": None,
    "mt.opengl": None,
    "mt.glm": None,
    "mt.imageio": None,
    "mt.iio": None,
    "mt.v4l2": None,
    "mt.struct": None,
}

master_doc = "index"


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
