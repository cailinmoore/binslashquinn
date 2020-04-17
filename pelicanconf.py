#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Quinn Handley'
SITENAME = '/bin/quinn'
#SITEURL = 'http://binslashquinn.com'
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%m.%d.%Y'

PATH = 'content'
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True

# Plugins
PLUGIN_PATHS = ["plugins"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = "themes/pelican-hss"
TAGLINE = 'Software developer, alpinist, contemplater of things'
USER_LOGO_URL = SITEURL + '/images/me2.png'

# Social widget
SOCIAL = (  ('github', 'https://github.com/qhandley'),
            ('linkedin', 'https://linkedin.com/in/quinnhandley'),
            ('twitter', 'https://twitter.com/q_handley'), )

DEFAULT_PAGINATION = 5 

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
