# -*- coding: utf-8 -*-
# Note: All configuration keys have to be in caps.
AUTHOR = u'Tony S. Yu'
SITENAME = u"Tony S. Yu"
SITEURL = 'http://tonysyu.github.com'
SITETAG = u":-T"
COPYRIGHT = "&copy; 2014 Tony S. Yu."
TIMEZONE = "America/New_York"
#LOGOIMAGE = 'theme/logo.png'
#LOGOTEXT = u":-T"

GITHUB_URL = 'http://github.com/tonysyu/'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 2
# Setting this permalink structure screws up links in "pages" somehow.
#ARTICLE_PERMALINK_STRUCTURE = '/%Y/'

#FEED_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (
    ('About me', 'pages/about-me.html'),
    ('Research', 'pages/research.html'),
    ('Articles', 'index.html'),
    ('Design', 'pages/design.html'),
    #('Art', 'pages/art.html'),
 )

# currently unused:
ALT_LINKS = (('github', 'http://github.com/tonysyu'),)

# static paths will be copied under the same name
STATIC_PATHS = ['images', 'includes']

# A list of files to copy from the source to the destination
# FILES_TO_COPY = [('CNAME', 'CNAME')]

# Tracker ID for Google Analytics
GOOGLE_ANALYTICS = 'UA-29631580-1'

# Disqus "shortname" for comments
DISQUS_SHORTNAME = 'tonysyu'
