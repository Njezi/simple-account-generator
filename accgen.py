import random
import os
import secrets

l = 'qwertyuiopasdfghjklzxcvbnm'
u = 'QWERTYUIOPASDFGHJKLZXCVBNM'
s = '!@#$%^&*()'
n = '1234567890'

pwd = ''
namegen = ''

#User settings
nickname_length = 10
password_length = 20

# l - lowercase u - uppercase s - symbols n - numbers
name_random = l + u + n
pw_random = l + u + s + n


for i in range(nickname_length):
  namegen += ''.join(secrets.choice(name_random))



for i in range(password_length):
  pwd += ''.join(secrets.choice(pw_random))

print("Your nickname is: " + namegen)
print("Your password is: " + pwd)