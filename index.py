import os
import time
import sys
from colorama import Fore, Style
os.system("clear")
print("BẠN CÓ CHẮC CHẮN MUỐN INSTALL HNMENU VÌ LÀ ĐANG LÀ OPEN BETA NÊN SẼ CÓ PHÁT SINH 1 SỐ LỖI KHÔNG MONG MUỐN NẾU BẠN PHÁT HIỆN ĐƯỢC VUI LÒNG LIÊN HỆ THÔNG TIN GITHUB BÊN DƯỚI\nCẢNH BÁO NẾU BẠN CHỈNH SỬA FILE THÌ MỌI THỨ SẼ LỖI!\n")
rt = input("Y/N:")
if rt =='y':
	os.system("clear")
	os.system("pkg install git")
	os.system("pip install colorama")
	os.system("python tar.py")
elif rt =='Y':
	os.system("clear")
	os.system("pkg install git")
	os.system("pip install colorama")
	os.system("python tar.py")
elif rt =='n':
	os.system("clear")
	quit()
elif rt =='N':
	os.system("clear")
	quit()