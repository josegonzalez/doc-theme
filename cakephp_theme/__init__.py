import os

__version__ = '0.0.0'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir


def update_context(app, pagename, templatename, context, doctree):
    context['cakephp_theme_version'] = __version__


def setup(app):
    app.connect('html-page-context', update_context)
    return {'version': __version__,
            'parallel_read_safe': True}
