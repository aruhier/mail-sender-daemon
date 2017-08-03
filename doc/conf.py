# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# extranet documentation build configuration file, created by
# sphinx-quickstart on Tue Feb  3 10:01:13 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sphinx_rtd_theme
import os
import sys

sys.path.insert(0, os.path.abspath('../'))

# -- General configuration ------------------------------------------------

# needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'Mail Sender'
copyright = '2017, Anthony25 <Anthony Ruhier>'

version = '0.1.0'
release = '0.1.0'

language = 'en'
locale_dirs = ['locale/']
gettext_compact = False

exclude_patterns = ['_build']

pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_show_sphinx = True
html_show_copyright = True
htmlhelp_basename = 'callbillingdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'mail_sender.tex', 'Mail Sender Documentation',
   'Anthony Ruhier', 'manual'),
]

latex_use_parts = False
latex_show_pagerefs = False


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'Mail Sender', 'Mail Sender Documentation',
     ['Anthony Ruhier'], 1)
]

man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Mail Sender', 'Mail Sender Documentation',
   'Anthony Ruhier', 'Mail Sender',
   'Send mail through different providers with autofailover.',),
]

texinfo_appendices = []
texinfo_domain_indices = True
texinfo_show_urls = 'footnote'
texinfo_no_detailmenu = False


def setup(app):
    app.add_stylesheet("theme_override.css")
