import random
import pyperclip

text = '1234567890QWERTYUIOP[]\ASDFGHJKLZXCVBNM./qwertyuiopasdfghjklzxcvbnm;:<>?{}#%!()_-=+'
alphabet = list(text)
list = random.sample(alphabet, k=20)
password = ''.join(list)

print("heres your password:", password)

retry = input('do you want to retry? y/n ')

if retry == 'y':
    print("heres your password:", password)

    copy = input('do you want to copy it? y/n ')
    if copy == 'y':
        pyperclip.copy(password)
        print('copied it.')
        input('Press enter to quit.')
        quit()
    else:
        input('Press enter to quit.')
        quit()
else:
    copy = input('do you want to copy it? y/n ')
    if copy == 'y':
        pyperclip.copy(password)
        print('copied it.')
        input('Press enter to quit.')
        quit()
    else:
        input('Press enter to quit.')
        quit()