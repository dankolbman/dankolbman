AUTHOR = "Dan Kolbman"
SITENAME = "Dan Kolbman"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

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
    ("GitHub", "https://github.com/dankolbman", "github.svg", "blue"),
    ("Adventures", "https://dankolbman.xyz", "globe.svg", "green"),
)

DEFAULT_PAGINATION = False

NOUNS = ("Developer", "Designer", "Architect")

BIO = """ """

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = "theme"
THEME_STATIC_DIR = "theme"
