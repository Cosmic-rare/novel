'''
モジュールのインポート
'''
from bs4.element import NavigableString
from mode.all import mode_all
import time
from urllib import request
import time
from bs4 import BeautifulSoup
import os
import re
from tqdm import tqdm
import ssl
import sys

from func import check_url, setup

from mode.all import mode_all

'''引き数の取得'''
args = sys.argv
if 3 <= len(args):
    if args[2].isdigit():

        if check_url('https://ncode.syosetu.com/novelview/infotop/ncode/{}/'.format(args[1])):
            setup(args[1])
            if args[2] == "1":
                mode_all(args[1])
            elif args[2] == "2":
                print("2")
            elif args[2] == "3":
                print("3")
            else:
                print("mode Error")
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
