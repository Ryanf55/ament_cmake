# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ament_cmake'
copyright = '2024, Ryan Friedman'
author = 'Ryan Friedman'
release = '2.3.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://gitlab.com/Pro1/doxygen-cmake-sphinx/-/blob/master/doc/conf.py.in
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    # Could not import extension sphinx_sitemap (exception: No module named 'sphinx_sitemap')
    # 'sphinx_sitemap',
    'sphinx.ext.inheritance_diagram',
    # Could not import extension breathe (exception: No module named 'breathe')
    # 'breathe',
    'sphinxcontrib.moderncmakedomain'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for generating CMake docs --------------------------------------

# cmake.__dir__
