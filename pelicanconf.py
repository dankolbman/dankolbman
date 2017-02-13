#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan Kolbman'
SITENAME = 'Dan Kolbman'
SITEURL = ''

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'dan@kolbman.com'),
    ('github', 'https://github.com/dankolbman'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

BIO = ""
PROFILE_IMAGE = "dankolbman.jpg"

THEME = "pelican-themes/hyde"

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
