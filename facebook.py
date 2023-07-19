import time
import os
import sys
from colorama import Fore, Style
os.system("clear")
a = '1.TDS Facebook\n2.TDS page pro5\n3.Tiện ích khác\n4.Thoát'
print(Fore.YELLOW + a)
rt = input("Lựa chọn:")
if rt =='1':
	os.system("python tds.py")
elif rt=='2':
	os.system("python pro5.py")
elif rt =='4':
	os.system("python menu.py")