import random

def randopwd():
    print('Welcome to Jonathan\'s Password Generator')

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'
    sym = '!@#$%^&*(),.?'

    chars = lower + upper + num + sym

    # get input and ensure input is int
    
    
    for attempts in range(3):
        length = input('# of characters that your password requires:')
        try:
            int(length)
        except:
            print("Please enter an integer in numerical form.")
            continue
        else:
            break

    pwd = ''
    for i in range(int(length)):
        pwd += random.choice(chars)
    print(pwd)
randopwd()