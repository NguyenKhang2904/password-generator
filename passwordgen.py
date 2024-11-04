import random
import pyperclip
text = '1234567890QWERTYUIOP[]\ASDFGHJKLZXCVBNM./qwertyuiopasdfghjklzxcvbnm;:<>?{}#%!()_-=+'
alphabet = list(text)
list = random.sample(alphabet, k=20)
password = ''.join(list)
print("heres your password:", password)
pyperclip.copy(password)
input()