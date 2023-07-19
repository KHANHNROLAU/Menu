import os
import sys
from colorama import Fore, Style
os.system("clear")
print("1.Tiktok Buff View\n2.Tiktok Buff lưu\n3.TDS Tiktok\n4.Thoát")
rt = input("Lựa chọn:")
if rt =='1':
	os.system("python tool2.py")
elif rt =='2':
	os.system("python tool3.py")
elif rt =='3':
	os.system("python tool4.py")
elif rt =='4':
	os.system("python menu.py")