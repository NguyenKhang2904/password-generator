import random
import pyperclip

text = '1234567890QWERTYUIOP[]\ASDFGHJKLZXCVBNM./qwertyuiopasdfghjklzxcvbnm;:<>?{}#%!()_-=+'
alphabet = list(text)
list = random.sample(alphabet, k=20)
password = ''.join(list)

print("Here's your password:", password)

retry = input('Do you want to retry? y/n ')

if retry == 'y':
    print("Here's your password:", password)

    copy = input('Do you want to copy it? y/n ')
    if copy == 'y':
        pyperclip.copy(password)
        print('Copied.')
        input('Press enter to quit.')
        quit()
    else:
        input('Press enter to quit.')
        quit()
else:
    copy = input('Do you want to copy it? y/n ')
    if copy == 'y':
        pyperclip.copy(password)
        print('Copied.')
        input('Press enter to quit.')
        quit()
    else:
        input('Press enter to quit.')
        quit()