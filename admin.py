import os
import sys
import time
from colorama import Fore, Style
os.system("clear")
a = '''How to run?\ntamp-start:Run Tamp\ntamp-stop:Stop tamp\nmenu:Run menu admin'''
print(Fore.RED + a)
rt = input(Fore.WHITE + "Command:")
if rt=='tamp-start':
	os.system("python tamp0.py")
elif rt=='tamp-stop':
	os.system("python tamp1.py")
elif rt=='menu':
	os.system("python menu.py")