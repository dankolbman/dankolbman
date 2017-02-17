#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Kolbman'
SITENAME = 'Daniel Kolbman'
SITEURL = ''

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './'
PLUGINS = ['pelican-ipynb.markup']

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['posts', 'images', 'KolbmanCapII.pdf', 'favicon.ico']
EXTRA_PATH_METADATA = { 'favicon.ico': {'path': 'favicon.ico'} }

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
        Hey! I'm Dan Kolbman.

        I'm an engineer at the
        <a href="http://cdis.uchicago.edu/">Center for Data Intensive Science</a>
        at the University of Chicago where I work on applications to distribute
        and analyze large scale genomics data for the
        <a href="https://gdc.cancer.gov/">Genomic Data Commons</a>.

        I studied Physics at the Rochester Institute of Technology where I created a
        <a href="https://github.com/dankolbman/BCIM">dynamics simulation</a>
        using high performance computing to model
        <a href="/KolbmanCapII.pdf">cancer cell mechanics</a>.

        In my free time, I like take a break from the all that serious science
        to do things like write bots to crawl through
        <a href="https://github.com/dankolbman/CleverTind">dating apps</a>.

        I'm an advocate of Open Source/Open Science and publish most of my work
        <a href="https://github.com/dankolbman">freely</a>.

        I gorge on tea and coffee, listen to techno religiously, and
        <a href="http://dankolbman.xyz">travel the world</a>.
      """

SIDEBAR_BIO = """Engineer Extraordinaire"""

PROFILE_IMAGE = "dankolbman.jpg"

THEME = "pelican-hyde"

DEFAULT_PAGINATION = 1
