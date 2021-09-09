import time
import urllib
import time
from bs4 import BeautifulSoup
import re
from tqdm import tqdm

def check_url(url):
# urlが存在する場合Trueを返す
    try:
        urllib.request.urlopen(url)
    except (urllib.error.URLError, urllib.error.HTTPError):
        return False
    else:
        return True

def get_parts(ncode):
    while True:
        start = input('Start > ')
        end = input('End > ')
        start_url = 'https://ncode.syosetu.com/{}/{}'.format(ncode, start)
        end_url = 'https://ncode.syosetu.com/{}/{}'.format(ncode, end)
        if check_url(start_url) and check_url(end_url):
            break
    return int(start), int(end)

def mode_range(ncode):
    start, end = get_parts(ncode)
    parts = end - start + 1

    # 進捗バーの設定
    bar = tqdm(total=parts)

    for i in range(start, end+1):
        res_url = 'https://ncode.syosetu.com/{}/{:d}'.format(ncode, i)
        
        # リクエストして解析
        res = urllib.request.urlopen(res_url)
        soup = BeautifulSoup(res, 'html.parser')
        honbun = soup.select_one('#novel_honbun').text

        # 改行コードを変換する
        honbun = honbun.replace('\n', '\r\n')

        # ページ数のファイルを生成する
        with open(ncode + '/' + str(i) + '.txt', 'w', encoding='shift_jis') as fr:
            pass

        # 一文字ずつ保存していく
        with open(ncode + '/' + str(i) + '.txt', 'w', encoding='shift_jis') as fr:
            for j in honbun:
                try:
                    fr.write(j)
                except:
                    fr.write('?')
        
        # 進捗を更新 => 待つ
        bar.update(1)
        time.sleep(0.75)

