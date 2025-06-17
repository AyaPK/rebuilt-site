AUTHOR = 'Aya Stead'
SITENAME = 'Aya Stead'
SITESUBTITLE = 'I like making cool things!'
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

)

# Social widget
SOCIAL = (
    ('fa-brands fa-linkedin-in', 'LinkedIn', 'https://linkedin.com/in/aya-s-stead'),
    ('fa-regular fa-envelope', 'Email me', 'mailto:aya@ayasca.dev'),
    ('fa-brands fa-github', 'GitHub', 'https://github.com/ayapk'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

import os
THEME = os.path.join(os.path.dirname(__file__), 'theme')

from datetime import datetime
LAST_UPDATED = datetime.now().strftime('%Y-%m-%d')

# Menu items for navbar
MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Update History', '/update-history.html'),
    ('Personal Projects', '/pages/personal-projects.html'),
    ('Non-Coding Hobbies', '/pages/hobbies.html'),
    # Add more items as needed
)

# To only show these items, set DISPLAY_PAGES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False