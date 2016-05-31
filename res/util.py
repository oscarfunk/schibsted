import sys
from contextlib import closing

import lxml.html as html # pip install 'lxml>=2.3.1'
from lxml.html.clean        import Cleaner
from selenium.webdriver     import Firefox         # pip install selenium
from werkzeug.contrib.cache import FileSystemCache # pip install werkzeug

cache = FileSystemCache('.cachedir', threshold=100000)

url = sys.argv[1] if len(sys.argv) > 1 else "http://www.schibsted.cl/testqa/"


# get page
page_source = cache.get(url)
if page_source is None:
    # use firefox to get page with javascript generated content
    with closing(Firefox()) as browser:
        browser.get(url)
        page_source = browser.page_source
    cache.set(url, page_source, timeout=60*60*24*7) # week in seconds


# extract text
root = html.document_fromstring(page_source)
# remove flash, images, <script>,<style>, etc
Cleaner(kill_tags=['noscript'], style=True)(root) # lxml >= 2.3.1
webtext = root.text_content() # extract text
f = open("C:/schibsted/data/Test.txt", "w");
print f
value = (webtext)
myString = str(value)
f.write(myString)
f.close()


