# -*- coding: utf-8 -*-
import datetime
import sys
import os
import cakephp_theme
from sphinx.highlighting import lexers
from pygments.lexers.php import PhpLexer

########################
# Begin Customizations #
########################

maintainer = u'Cake Software Foundation, Inc.'
project = u'doc-theme'
project_pretty_name = u'CakePHP Doc Theme'
copyright = u'%d, CakePHP' % datetime.datetime.now().year
version = '0.0.2'
release = '0.0.2'
html_title = 'CakePHP Doc Theme'
html_context = {
    'maintainer': maintainer,
    'project_pretty_name': project_pretty_name,
    'projects': {
        'CakePHP Book': 'https://book.cakephp.org/',
        'Doc Theme': 'https://cakephp-theme.readthedocs.io/',
    }
}

htmlhelp_basename = 'doc-theme'
latex_documents = [
    ('index', 'doc-theme.tex', u'doc-theme',
     u'CakePHP', 'doc-theme'),
]
man_pages = [
    ('index', 'doc-theme', u'CakePHP Doc Theme Documentation',
     [u'CakePHP'], 1)
]

texinfo_documents = [
    ('index', 'crud-view', u'CakePHP Doc Theme Documentation',
     u'CakePHP', 'crud-view', 'A Sphinx theme for CakePHP doc sites',
     'Miscellaneous'),
]

branch = 'master'

########################
#  End Customizations  #
########################

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.phpdomain',
    'cakephp_theme',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'contents'
exclude_patterns = [
    '_build',
    '_themes',
    '_partials',
]

pygments_style = 'sphinx'
highlight_language = 'php'

# -- Options for HTML output ----------------------------------------------

html_theme = 'cakephp_theme'
html_theme_path = [cakephp_theme.get_html_theme_path()]
html_static_path = []
html_last_updated_fmt = '%b %d, %Y'
html_sidebars = {
    '**': ['globaltoc.html', 'localtoc.html']
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

lexers['php'] = PhpLexer(startinline=True)
lexers['phpinline'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
primary_domain = "php"
