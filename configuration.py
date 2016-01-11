#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan Kolbman'
SITENAME = 'Dan Kolbman'
SITESUBTITLE = ''
SITEBLURB = '''Hey! I'm Dan Kolbman. I studied Physics at the Rochester Institute
            of Technology. While there, I created a
            <a href="https://github.com/dankolbman/BCIM">dynamics simulation</a>
            using high performance computing to model
            <a href=http://google.com>cancer cell mechanics</a>
            '''
SITEURL = ''

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = 'plugins'
PLUGINS = ['ipynb']

MD_EXTENSIONS = ['codehilite', 'extra']

GITHUBURL = 'https://github.com/dankolbman'
TWITTERURL = 'https://twitter.com/DanKolbman'
TRACKERURL = 'http://dankolbman.com'

PATH = 'content'
THEME = 'theme'

# I'm storing each post and it's images inside a subfolder inside posts
# so I'd like to both create pages from the posts as well as preserve the other
# files and their paths in the post's directory
STATIC_PATHS = ['posts', 'extra/favicon.ico']
ARTICLE_PATHS = ['posts']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/README.md' : {'path': 'README.md'}
}

ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
ARTICLE_URL = 'articles/{slug}/index.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 6

USE_FOLDER_AS_CATEGORY = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
