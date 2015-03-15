#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Wagner'
SITENAME = u'Adam Wagner'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "theme"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

"""
List of templates that are used directly to render content. Typically direct templates are used to generate index pages for collections of content (e.g., tags and category index pages). If the tag and category collections are not needed, set DIRECT_TEMPLATES = ('index', 'archives')
"""
# DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')


