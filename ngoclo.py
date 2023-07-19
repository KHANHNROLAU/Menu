import os
import sys
import time
from colorama import Fore, Style
os.system("clear")
a = '''1.Bản offline'''
print(Fore.YELLOW + a)
rt = input("Lựa chọn:")
if rt =='1':
	print("Đang bảo trì chức năng!")
	time.sleep(2)
	os.system("python menu.py")