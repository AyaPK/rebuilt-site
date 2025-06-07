AUTHOR = 'Aya Stead'
SITENAME = 'Aya Stead'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('GitHub', 'https://github.com/ayapk'),
    ('LinkedIn', 'https://linkedin.com/in/aya-s-stead'),
)

# Social widget
SOCIAL = (
    ('envelope', 'mailto:aya.pk.contact@gmail.com'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

import os
THEME = os.path.join(os.path.dirname(__file__), 'theme')

from datetime import datetime
LAST_UPDATED = datetime.now().strftime('%Y-%m-%d')