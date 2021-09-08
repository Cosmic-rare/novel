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

def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True

def get_part(ncode):
    while True:
        part = input('Part > ')
        if isint(part):
            url = 'https://ncode.syosetu.com/{}/{:d}'.format(ncode, int(part))
            if check_url(url):
                break
    
    return int(part)