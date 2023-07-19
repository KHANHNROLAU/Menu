import os
import sys
from colorama import Fore, Style
os.system("clear")
a = '''1.Tds Facebook loại 1\n2.Tds Facebook Full job\n3.Thoát'''
print(Fore.YELLOW + a)
rt = input("Lựa chọn:")
if rt=='1':
	os.system("python tool5.py")
elif rt =='2':
	os.system("python tool6.py")
elif rt=='3':
	os.system("python facebook.py")