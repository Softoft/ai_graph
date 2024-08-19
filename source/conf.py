import os
import sys
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
sys.path.insert(0, os.path.abspath('../'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AI Graph'
copyright = '2024, Tobi A. Bück'
author = 'Tobi A. Bück'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []
html_theme = "sphinx_rtd_theme"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary'
]
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# Order members by the order they appear in the source code
autodoc_member_order = 'bysource'

# Autodoc default options
autodoc_default_options = {
    'members': True,
    'special-members': '__init__',
    'undoc-members': True,
    'show-inheritance': True,
}
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
