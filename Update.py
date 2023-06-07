import os


print('--------> Downloading configer.py\n\n')
os.system('curl -Lo /root/configer/configer.py https://raw.githubusercontent.com/M0HMD-M/sing-box-tg-bot-configer/master/configer.py')
os.system('systemctl restart configer.service')
print('Done, enjoy!')
