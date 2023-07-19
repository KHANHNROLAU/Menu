import os
import sys
import time
from colorama import Fore, Style
os.system("clear")
banner = '''██╗     ██╗ ██████╗ ██╗   ██╗███████╗                        
██║     ██║██╔═══██╗██║   ██║██╔════╝                        
██║     ██║██║   ██║██║   ██║█████╗                          
██║     ██║██║▄▄ ██║██║   ██║██╔══╝                          
███████╗██║╚██████╔╝╚██████╔╝███████╗                        
╚══════╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝                        
███████╗██╗  ██╗ █████╗ ██╗    ██╗██████╗  ██████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██║    ██║██╔══██╗██╔═══██╗██║    ██║
███████╗███████║███████║██║ █╗ ██║██║  ██║██║   ██║██║ █╗ ██║
╚════██║██╔══██║██╔══██║██║███╗██║██║  ██║██║   ██║██║███╗██║
███████║██║  ██║██║  ██║╚███╔███╔╝██████╔╝╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═════╝  ╚═════╝  ╚══╝╚══╝ 
'''
scr = '''                                                                               
███████╗███████╗███████╗███████╗███████╗███████╗
╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝'''
print(Fore.BLUE  + banner)
print(Fore.YELLOW + scr)
print(Fore.YELLOW + "1.Spam mess\n2.Spam sms+Call\n3.Tiện ích tiktok\n4.Ngọc cltool3.2\n5.Facebook")
rt = input("Lựa chọn:")
if rt =='1':
	os.system("python tool0.py")
elif rt =='2':
	os.system("python tool1.py")
elif rt =='3':
	os.system("python tiktok.py")
elif rt=='4':
	os.system("python ngoclo.py")
elif rt =='5':
	os.system("python facebook.py")