import random

l = 'qwertyuiopasdfghjklzxcvbnm'
u = 'QWERTYUIOPASDFGHJKLZXCVBNM'
s = '!@#$%^&*()'
n = '1234567890'

pwdgen = ''
namegen = ''

# User settings
nickname_length = 10
password_length = 20

# l - lowercase u - uppercase s - symbols n - numbers
name_random = l + u + n
pw_random = l + u + s + n


# Generate the nickname and password
for i in range(nickname_length):
  namegen += ''.join(random.choice(name_random))

for i in range(password_length):
  pwdgen += ''.join(random.choice(pw_random))


# Print out the generated nickname and password
print("Your nickname is: " + namegen)
print("Your password is: " + pwdgen)