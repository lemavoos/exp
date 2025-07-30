import os
import sys
import platform

def indentfy_os(): #Indentify OS
    if platform.system () == 'Windows':
        os.system('exploit.bat')
    else:
        os.system('chmod +x exploit.sh && ./exploit.sh')

def install_ssh():
    if platform.system() == 'Windows':
        os.system('err')
    else:
        os.system('sudo pkg install openssh -y')
        os.system('sshd')
        print("Insert password for root user:")
        os.system('passwd')