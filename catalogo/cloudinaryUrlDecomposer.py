import re

def decompose(url=''):
    r_key = r'://(.*?):(.*?)@(.*)'

    matches = re.search(r_key, url)

    cloudinary_url_parms = {
    'key'   : matches.group(1),
    'secret': matches.group(2),
    'name'  : matches.group(3),
    }
    return cloudinary_url_parms