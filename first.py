import pickle
import os
import sys
import subprocess
from subprocess import Popen, PIPE
import time


if not os.path.exists('/root/configer'):
    os.system('mkdir configer')
os.system('curl -Lo /root/cleaner.py https://raw.githubusercontent.com/M0HMD-M/sing-box-tg-bot-configer/master/cleaner.py')
os.system('python3 /root/cleaner.py')
os.system('rm /root/cleaner.py')
# Get sing-box v1.3 beta12 and place it in root
print('--------> 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒊𝒏𝒈 𝒔𝒊𝒏𝒈-𝒃𝒐𝒙:\n\n\n\n')
subprocess.run(["bash", "-c", "curl -Ls https://raw.githubusercontent.com/FranzKafkaYu/sing-box-yes/master/install.sh | bash -s install 1.3-beta12"], check=True)
print('-------- 𝑰𝒏𝒔𝒕𝒂𝒍𝒍𝒊𝒏𝒈 𝒔𝒊𝒏𝒈-𝒃𝒐𝒙 𝒇𝒊𝒏𝒊𝒔𝒉𝒆𝒅 ✔ --------\n\n')

print('--------> 𝑪𝒓𝒆𝒂𝒕𝒊𝒏𝒈 𝒖𝒔𝒆𝒓_𝒅𝒂𝒕𝒂 ^_^\n\n')
user_data = {
    "chat_id":"me",
    "user_id":"",
    "channel_id": "",
    "server_IP": "",
    "listen_port": 443,
    "bot_token": "",
    "renewal_interval":0,
    "domain_name":'domain.com'
}
try:
    user_data["bot_token"] = sys.argv[1]
except:
    user_data["bot_token"] = input("/////////// Enter bot token: ")
finally:
    with open("/root/configer/user_data.pkl", "wb") as f:
        pickle.dump(user_data, f)
        print(f"-------user_data was created!-------\n{user_data}\n\n")



print('--------> Downloading configer.py\n\n')
os.system('curl -Lo /root/configer/configer.py https://raw.githubusercontent.com/M0HMD-M/sing-box-tg-bot-configer/master/configer.py')
os.system('curl -Lo /root/configer/user_data_editor.py https://raw.githubusercontent.com/M0HMD-M/sing-box-tg-bot-configer/master/user_data_editor.py')
os.system('apt-get -y install pip')
os.system('pip install python-telegram-bot==13.5')
os.system('pip install requests')
time.sleep(1)
time.sleep(1)
if not os.path.exists('/etc/systemd/system/configer.service'):
    print('--------> Setting up Services \n\n')
    os.system('curl -Lo /etc/systemd/system/configer.service https://raw.githubusercontent.com/M0HMD-M/sing-box-tg-bot-configer/master/configer.service')
    os.system('systemctl daemon-reload')
    os.system('sleep 0.2')
    os.system('systemctl enable configer.service')
    os.system('sleep 0.2')
    os.system('systemctl start configer.service')
else:
    os.system('systemctl restart configer.service')
default_config_path = '/usr/local/etc/sing-box/config.json'
if os.path.exists(default_config_path):
    os.system(f'rm {default_config_path}')
os.system('systemctl restart configer')
os.system('systemctl restart sing-box')
print('-------- 𝙎𝙚𝙩𝙩𝙞𝙣𝙜 𝙪𝙥 𝙎𝙚𝙧𝙫𝙞𝙘𝙚𝙨 𝙛𝙞𝙣𝙞𝙨𝙝𝙚𝙙 ✔ --------\n\n')

s = '''

  _    _                   ______             __  
 | |  | |                 |  ____|            \ \ 
 | |__| | __ ___   _____  | |__ _   _ _ __   (_) |
 |  __  |/ _` \ \ / / _ \ |  __| | | | '_ \    | |
 | |  | | (_| |\ V /  __/ | |  | |_| | | | |  _| |
 |_|  |_|\__,_| \_/ \___| |_|   \__,_|_| |_| (_) |
                                              /_/ 
                                                                                                         
'''

print(s)
print('\n\n-------->  𝑺𝒆𝒏𝒅 /𝒔𝒕𝒂𝒓𝒕 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒕𝒐 𝒚𝒐𝒖𝒓 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒃𝒐𝒕')
print('\n\n-------->  𝘈𝘧𝘵𝘦𝘳 𝘵𝘩𝘢𝘵 : ')
print('\n\n-------->  𝗦𝗲𝗻𝗱 /𝘀𝗲𝘁  𝘁𝗼 𝘀𝗲𝘁 𝘆𝗼𝘂𝗿 𝗽𝗿𝗲𝗳𝗿𝗲𝗻𝗰𝗲𝘀')
mmd = '''


 ____    ____     ____     ____  ____   ____    ____   ______              ____    ____  
|_   \  /   _|  .'    '.  |_   ||   _| |_   \  /   _| |_   _ `.           |_   \  /   _| 
  |   \/   |   |  .--.  |   | |__| |     |   \/   |     | | `. \  ______    |   \/   |   
  | |\  /| |   | |    | |   |  __  |     | |\  /| |     | |  | | |______|   | |\  /| |   
 _| |_\/_| |_  |  `--'  |  _| |  | |_   _| |_\/_| |_   _| |_.' /           _| |_\/_| |_  
|_____||_____|  '.____.'  |____||____| |_____||_____| |______.'           |_____||_____| 
                                                                                         
'''
print(mmd)
