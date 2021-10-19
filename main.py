from bs4.element import NavigableString
from mode.all import mode_all
import time
from urllib import request
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys

from func import check_url, setup, get_part

from mode.all import mode_all
from mode.one_page import mode_one
from mode.range import mode_range

args = sys.argv
if 3 <= len(args):
    if args[2].isdigit():

        if check_url('https://ncode.syosetu.com/novelview/infotop/ncode/{}/'.format(args[1])):
            setup(args[1])
            if args[2] == "1":
                mode_all(args[1])
            elif args[2] == "2":
                mode_range(args[1])
            elif args[2] == "3":
                mode_one(args[1], get_part(args[1]))
            else:
                print("mode Error")
        else:
            print('ncode Error')

    else:
        print('Argument is not digit')
else:
    print('Arguments are too short')
