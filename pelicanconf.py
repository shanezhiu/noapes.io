#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shane Chiu'
SITENAME = "Noapes' blog"
SITESUBTITLE = 'Stay hungry, Stay foolish'

PATH = 'content'
PAGE_PATHS=['pages']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Time and Date
DEFAULT_DATE = 'fs'

# Theme
THEME = 'themes/pelican-alchemy/alchemy'

SITEIMAGE = '/images/profile.jpeg width=200 height=200'

STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
}
# sumary max length 
# SUMMARY_MAX_LENGTH = 30
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

# tralstions
# The default language to use.
DEFAULT_LANG = 'en'
# The metadata attribute(s) used to identify which articles are translations of one another.
ARTICLE_TRANSLATION_ID = 'slug'

# Extra configuration settings for the Markdown processor.
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
# Plugins
PLUGINS = []
PLUGIN_PATHS = []
# A list of directories to exclude when looking for articles in addition to PAGE_PATHS
ARTICLE_EXCLUDES = [
    'drafts'
]

# Blogroll
# LINKS = (
#     ('Index', '/'),
#     ('About', '/pages/about.html'),
#     )

# ICONS 
ICONS = [
    ('github', 'https://github.com/shanezhiu'),
    ('stack-overflow', 'https://stackoverflow.com/users/2671683/shanechiu'),
    ('twitter', 'https://twitter.com/shanezhiu'),
    ('reddit', 'https://www.reddit.com/user/shanechiu'),
]

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PYGMENTS_STYLE = 'monokai'

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True~
DISPLAY_PAGES_ON_MENU = True