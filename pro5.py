import os
import sys
from colorama import Fore, Style
os.system("clear")
a = '1.Reg page pro5\n2.Ttc Page pro5\n3.TDS Page pro5\n4.Buff Follow Bằng page pro5\n5.Buff View Story bằng page pro5\n6.Chuyển quyền admin page pro5\n7.Thoát'
print(Fore.YELLOW + a)
rt = input("Lựa chọn:")
if rt =='1':
	os.system("python tool7.py")
elif rt =='2':
	os.system("python tool8.py")
elif rt =='3':
	os.system("python tool9.py")
elif rt=='4':
	os.system("python tool10.py")
elif rt=='5':
	os.system("python tool11.py")
elif rt =='6':
	os.system("python tool12.py")
elif rt =='7':
	os.system("python facebook.py")