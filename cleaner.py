import os 

# Stop Services
try:
    os.system('systemctl disable configer')
    os.system('systemctl disable sing-box')
except Exception as e:
      print(e)


# Remove files
files = ["/root/configer/user_data.pkl",
          "/root/configer/sb-data.json",
          "/root/configer/public_key.pkl",
          "/usr/local/etc/sing-box/config.json",
          "/root/configer/configer.py",
          "/root/user_data.pkl",
          "/root/sb-data.json",
          "/root/public_key.pkl",
          "/usr/local/etc/sing-box/config.json",
          "/root/configer.py",
          '/etc/systemd/system/configer.service',

          ]
for path in files:
    if os.path.exists(path):
            try:
                os.system(f'rm {path}')
                print(f'Delted {path}\n')
            except Exception as e:
                print(e)
            

