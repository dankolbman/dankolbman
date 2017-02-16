#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan Kolbman'
SITENAME = 'Dan Kolbman'
SITEURL = ''

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb']

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['posts', 'images']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SUMMARY_MAX_LENGTH = None

IPYNB_IGNORE_CSS = True
IPYNB_USE_META_SUMMARY = False

# Social widget
SOCIAL = (('email', 'dan@kolbman.com'),
          ('github', 'https://github.com/dankolbman'),
          ('globe', 'dankolbman.xyz'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

BIO = """
        Hey! I'm Dan Kolbman. I studied Physics at the Rochester Institute
        of Technology where I created a
        <a href="https://github.com/dankolbman/BCIM">dynamics simulation</a>
        using high performance computing to model
        <a href="/KolbmanCapII.pdf">cancer cell mechanics</a>.
      """
"""
In my free time, I like take a break from the all that serious science
and make silly web apps to help me find
<a href="https://github.com/foodsnag/foodsnag-web">free food</a>
or write bots to crawl through
<a href="https://github.com/dankolbman/CleverTind">dating apps</a>.
I'm an advocate of Open Source/Open Science and publish most of my work
<a href="https://github.com/dankolbman">freely</a>.
I gorge on tea and coffee, listen to techno religiously, and
<a href="http://dankolbman.xyz">travel the world</a>.
"""
PROFILE_IMAGE = "dankolbman.jpg"

THEME = "pelican-hyde"

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
