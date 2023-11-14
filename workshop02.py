
import random

def random_number():
    Number  = random.randint(1,100)

    while True:
        try:
            userInput =int(input('ทายตัวเลขที่มีค่าอยู่ 1-100:'))
            if userInput == Number:
                print('ยินด้วยคุณทายถูก')
                break 
            elif  userInput < Number:
                print('คุณทายตัวเลขน้อยไป')
            else:
                print('คุณทายผิดตัวเลขมากไป')
        except ValueError:
            print('โปรดป้อนตัวเลขเท่านั้น')

random_number()
