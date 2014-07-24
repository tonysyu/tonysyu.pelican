# -*- coding: utf-8 -*-
# Note: All configuration keys have to be in caps.
AUTHOR = u'Tony S. Yu'
SITENAME = u"Tony S. Yu"
SITEURL = 'http://tonysyu.github.io'
SITETAG = u":-T"
COPYRIGHT = "&copy; 2014 Tony S. Yu."
TIMEZONE = "America/New_York"
THEME = "/Users/tonysyu/Sites/pelican-themes/pelican-bootstrap3"

OUTPUT_PATH = 'output'

GITHUB_URL = 'http://github.com/tonysyu/'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 2

MENUITEMS = (
    ('About me', '/pages/about-me.html'),
    ('Research', '/pages/research.html'),
    ('Articles', '/index.html'),
    ('Design', '/pages/design.html'),
 )

LINKS = (
    ('Enthought', 'http://www.enthought.com/'),
    ('scikit-image', 'http://http://scikit-image.org/'),
    ('matplotlib', 'http://matplotlib.sourceforge.net/'),
 )

# currently unused:
ALT_LINKS = (('github', 'http://github.com/tonysyu'),)

CUSTOM_CSS = 'static/custom.css'
# static paths will be copied under the same name
STATIC_PATHS = ['images', 'includes', 'extra']
# Note that both EXTRA_PATH_METADATA and STATIC_PATHS are required
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

PYGMENTS_STYLE = 'friendly'

# A list of files to copy from the source to the destination
# FILES_TO_COPY = [('CNAME', 'CNAME')]

# Tracker ID for Google Analytics
GOOGLE_ANALYTICS = 'UA-29631580-1'

# Disqus "shortname" for comments
DISQUS_SHORTNAME = 'tonysyu'
