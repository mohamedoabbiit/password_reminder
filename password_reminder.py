import os
def clear(): return os.system('cls')


clear()

input_name = input("please enter your first, last name to remind your password: ")


word = {'Mohamed Abbi': 'moha2abbi2021'}
password = list(word.keys())

input_convert = list([input_name])


if password == input_convert:
    for key, val in word.items():
        print("Hello, {}! the password is: {}\n\n ".format(key, val))
else:
    print("Hello, {} see you later.\n\n ".format(input_name))
