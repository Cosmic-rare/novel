'''
モジュールのインポート
'''
import time
from urllib import request
import time
from bs4 import BeautifulSoup
import os
import re
from tqdm import tqdm
import ssl
import sys

from func import check_url

'''引き数の取得'''
args = sys.argv
if 3 <= len(args):
    if args[2].isdigit():

        if args[2] == "1":
            print("1")
        elif args[2] == "2":
            print("2")
        elif args[2] == "3":
            print("3")
        else:
            print("mode Error")

        if check_url('https://ncode.syosetu.com/novelview/infotop/ncode/{}/'.format(args[1])):
            pass
        else:
            print('ncode Error')

    else:
        print('Argument is not digit')
else:
    print('Arguments are too short')




# 全取得
# ページ指定はそのページのみ
# 範囲はまず入力
# 整数である＆存在するなら取ってくる
# ないならもう一度
# 辞書を指定するとパスを入力させる
# 入力されたパスに保存
# そうでない場合作って保存
