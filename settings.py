# -*- coding: utf-8 -*-
# NOTE: This project is configured for Pelican 3.x and is known to fail on
#       Pelican 2.x.
#
# Note: All configuration keys have to be in caps.
AUTHOR = u'Tony S. Yu'
SITENAME = u"Tony S. Yu"
SITEURL = 'https://tonysyu.github.io'
SITETAG = u":-T"
COPYRIGHT = "&copy; 2014 Tony S. Yu."
TIMEZONE = "America/New_York"

OUTPUT_PATH = 'output'
CUSTOM_CSS = 'static/custom.css'
THEME = "/Users/tyu/sites/pelican-themes/pelican-bootstrap3"

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
# Suppress auto-generated links in upper nav-bar.
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
# Number of posts per page
DEFAULT_PAGINATION = 5

ADDTHIS_PROFILE = 'ra-53f2c41705dd9003'

MENUITEMS = (
    ('About me', '/pages/about-me.html'),
    ('Articles', '/index.html'),
    ('Code', '/pages/code.html'),
    ('Research', '/pages/research.html'),
    ('Design', '/pages/design.html'),
)

LINKS = (
    ('github', 'http://github.com/tonysyu'),
    ('linkedin', 'https://www.linkedin.com/pub/tony-yu/48/600/130'),
)

# static paths will be copied under the same name
STATIC_PATHS = ['images', 'includes', 'extra']
# Note that both EXTRA_PATH_METADATA and STATIC_PATHS are required
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

ABOUT_BANNER = """
<div id="about">
    <div class="split-left">
        <img class="sidebar"
            src="http://tonysyu.github.io/images/tonysyu.jpg"
            width="120px"
            align="left"
            alt="Tony S. Yu">
    </div>

    <div class="split-right">
        <p class="sidebar">
            Software developer, engineer, and all-around good guy in
            Austin, TX, USA.
        </p>
    </div>
</div>
"""

PYGMENTS_STYLE = 'friendly'

# This seemed like a good idea, but it's pretty noisy.
# GITHUB_USER = 'tonysyu'
GITHUB_URL = 'http://github.com/tonysyu/'

# A list of files to copy from the source to the destination
# FILES_TO_COPY = [('CNAME', 'CNAME')]

# Tracker ID for Google Analytics
GOOGLE_ANALYTICS = 'UA-29631580-1'

# Disqus "shortname" for comments
DISQUS_SITENAME = 'tonysyu'
