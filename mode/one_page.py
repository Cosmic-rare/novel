from bs4.element import NavigableString
from urllib import request
from bs4 import BeautifulSoup


def mode_one(ncode, i):
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
    
