import vk_api
import time

print('===== VK AUTO OFFLINE =====')
login = input('Enter a login: ')
password = input('Enter a password: ')

vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

while True:
    vk.account.setOnline()
    print('Online!')
    time.sleep(150)
