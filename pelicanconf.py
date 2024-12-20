# Required imports
from datetime import datetime

# Define now() variable to print current year
NOW = datetime.now()

AUTHOR = 'Benjamin Patch'
SITENAME = 'Pelican Quickstart'
SITESUBTITLE = 'A Personal Blog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Theme
THEME = 'themes/bootstrap'
STYLESHEET_URL = '/theme/css/bootstrap.min.css'
ICON_STYLESHEET_URL = 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css'

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1.0,
        "indexes": 0.5,
        "pages": 0.3
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    },
    "exclude": [
        r"\.html$", # ends with ".html"
    ],
}

# Copy files into the root of 'output' directory
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
}
