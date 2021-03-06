import time
from urllib import request
import time
from bs4 import BeautifulSoup
import re
from tqdm import tqdm

def part(ncode):
    # ページ数を取得する
    url = 'https://ncode.syosetu.com/novelview/infotop/ncode/{}/'.format(ncode)
    res = request.urlopen(url)

    # 解析する
    soup = BeautifulSoup(res, 'html.parser')
    pre_info = soup.select_one('#pre_info').text

    # 正規表現でページ数を取得
    num_parts = int(re.search(r'全([0-9]+)部分', pre_info).group(1))

    return num_parts

def mode_all(ncode):
    parts = part(ncode)

    # 進捗バーの設定
    bar = tqdm(total=parts)

    for i in range(1, parts+1):
        res_url = 'https://ncode.syosetu.com/{}/{:d}'.format(ncode, i)
        
        # リクエストして解析
        res = request.urlopen(res_url)
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

