import urllib
import os

def setup(ncode):
    # ディレクトリの作成
    if not os.path.exists(ncode):
        os.makedirs(ncode)

def check_url(url):
# urlが存在する場合Trueを返す
    try:
        urllib.request.urlopen(url)
    except (urllib.error.URLError, urllib.error.HTTPError):
        return False
    else:
        return True