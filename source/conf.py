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


project = 'کتاب اودوو: اصول حسابداری ۱'
copyright = 'اودوونیکس ۱۴۰۴'
author = 'اودوونیکس'


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
html_js_files = []
html_context = {
    "rtl": True
}
html_show_sourcelink = False
html_theme_options={
    # Header links
    "external_links": [
        {
            "name": "Moonsun (Golden Odoo Partner)", 
            "url": "https://moonsun.au"
        },{
            "name": "Odoonix (OCA Partner)", 
            "url": "https://odoonix.com"
        },
    ],
    "header_links_before_dropdown": 2,

    # Navigation bar
    "show_nav_level": 3,
    "collapse_navigation": True,
    "navbar_start": [
        "navbar-logo", 
    ],
    
    # Page Table of Contents
    "show_toc_level": 2,

    # Sidebar items
    "secondary_sidebar_items": [
        "page-toc", 
        "sourcelink", 
        "version-switcher"
    ],
    "primary_sidebar_end": [
        "indices.html", 
        "sidebar-ethical-ads.html", 
        "version-switcher"
    ],

    # Github integration
    "use_edit_page_button": True,
    "check_switcher": False,
    "switcher": {
        "json_url": "https://odoonix.github.io/odoo-book-accounting/_static/versions.json",
        "version_match": "main",
    },

    # ADS
    "announcement": """
    ما را در توسعه و نگداری این کتاب
    <a href='https://odoonix.com/pages/donate'>
        حمایت مالی کنید! 
    </a>
    """,
    "show_version_warning_banner": True,
}
