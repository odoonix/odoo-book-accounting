"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------
import os
import sys

from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.locale import _

import pydata_sphinx_theme




sys.path.append(str(Path(".").resolve()))



project = 'Odoo Book: Accounting'
copyright = '2025, Odoonix'
author = 'Odoonix'


extensions = [
    # AutoAPI must run early to generate API files before other extensions
    # "autoapi.extension",
    # "sphinx.ext.napoleon",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    # "sphinx.ext.todo",
    # "sphinx.ext.viewcode",
    # "sphinx.ext.intersphinx",
    # "sphinx.ext.graphviz",
    # "sphinxext.rediraffe",
    # "sphinx_design",
    # "sphinx_copybutton",
    # custom extentions
    # "_extension.gallery_directive",
    # "_extension.component_directive",
    # For extension examples and demos
    # "myst_parser",
    # "ablog",
    # "jupyter_sphinx",
    # "sphinxcontrib.mermaid",
    # "sphinxcontrib.youtube",
    # "nbsphinx",
    # "numpydoc",
    # "sphinx_togglebutton",
    # "jupyterlite_sphinx",
    # "sphinx_favicon",
]
templates_path = ['_templates']
exclude_patterns = []
language = 'fa'



########################################################################################
# HTML THEME: odoonix_theme
# see: https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html
########################################################################################
html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_css_files = [
    'custom.css',
    'rtl.css'
]
html_context = {
    "rtl": True
}
html_theme_options={
    # direction = "ltr"
    # analytics_id = "UA-XXXXX-X"
    # website = ""
    # facebook = ""
    # googleplus = ""
    # linkedin = ""
    # twitter = ""
    # github = ""
    # gitlab = ""
    # bitbucket = ""
}
