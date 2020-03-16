from vk_api import exceptions, VkApi
from datetime import datetime
from time import sleep as slp

print('===== VK AUTO ONLINE =====')

login = input('Enter a login: ')
password = input('Enter a password: ')

vk_session = VkApi(login, password)

try:
    vk_session.auth()
except exceptions.BadPassword:
    print('Bad password!'); exit()

vk = vk_session.get_api()

try:
    while True:
        vk.account.setOnline()
        print(f'[{datetime.now().time().strftime("%H:%M:%S")}] You are online!')
        slp(45)
except KeyboardInterrupt:
    print('Exiting..'); exit()
