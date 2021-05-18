import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response
import webbrowser as web
import time
import random
import pandas as pd


data = pd.read_csv("prueba2.csv")
data_dict = data.to_dict('list')
celulares = data_dict['phone']
names = data_dict['nombre']
vacancy = data_dict['vacante']
skillone = data_dict['skillone']
skilltwo = data_dict['skilltwo']

combo = zip(celulares,names,vacancy,skillone,skilltwo)
first = True
for celulares,names,vacancy,skillone,skilltwo in combo:
    time.sleep(2)
    #web.open("https://web.whatsapp.com/send?phone=" + celulares)
    web.open("https://web.whatsapp.com/send?phone="+celulares+"&text="+'Hola '+names+', ' + '\n')
    if first:
        time.sleep(5)
    time.sleep(10)
    pt.typewrite('Actualmente estoy en busqueda de ' + vacancy + ' para un start up de XYZ.' + '\n')
    time.sleep(5)
    pt.typewrite('algunos de los beneficios son ....' + '\n' 'y las principales responsabilidades son ...' + '\n')
    time.sleep(5)
    pt.typewrite('Responde con la palabra "continuar" para avanzar en el primer filtro de seleccion.' + '\n')
    time.sleep(4)
    pt.hotkey('ctrl', 'r')
    time.sleep(2)


# Requires opencv-python package for image recognition confidence (in the near future)

# Mouse click workaround
mouse = Controller()



# Instructions for our WhatsApp Bot
class WhatsApp:
# Defines the starting values
    def __init__(self, speed=.8, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Navigate to the green dots for new messages
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ', e)

    # Navigate to our message input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 20, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)

    # Navigates to the message we want to respond to
    def nav_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(220, -150, duration=self.speed)  # x,y has to be adjusted depending on your computer
        except Exception as e:
            print('Exception (nav_message): ', e)

    # Copies the message that we want to process
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.keyDown('command')
        pt.press('c')
        pt.keyUp('command')
        #pt.moveRel(350, -20, duration=self.speed)  # x,y has to be adjusted depending on your computer

        # Gets and processes the message
        self.message = pc.paste()
        print('User says: ', self.message)

    # Sends the invite to a new candidate
    def send_invite(self):
        time.sleep(4)
        web.open("https://web.whatsapp.com/send?phone=" + celulares)
        #text = open('Hola'+ names + ',\n')
        #for word in text:
        #    pt.typewrite(word)
        #    pt.typewrite('enter')

    # Sends the message to the user
    def send_message(self):
        try:
            # Checks whether the last message was the same
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('You say: ', bot_response)
                pt.typewrite(bot_response, interval=.1)
                pt.typewrite('\n')  # Sends the message (Disable it while testing)

                # Assigns them the same message
                self.last_message = self.message
            else:
                print('No new messages...')

        except Exception as e:
            print('Exception (send_message): ', e)

    # Close response box
    def nav_x(self):
        try:
            position = pt.locateOnScreen('whatsapp_window.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            #pt.moveRel(100, -150, duration=self.speed)  # x,y has to be adjusted depending on your computer
            mouse.click(Button.right, 1)

        except Exception as e:
            print('Exception (nav_x): ', e)

        time.sleep(10)
        pt.hotkey('ctrl', 'w')

    # Update conversations
    def update_conv(self):
        time.sleep(4)
        pt.hotkey('ctrl', 'r')


# Initialises the WhatsApp Bot
wa_bot = WhatsApp(speed=.5, click_speed=.4)

inaloop = True
# Run the programme in a loop
while inaloop:
    for celulares in combo:
        time.sleep(4)
        web.open("https://web.whatsapp.com")
        time.sleep(1)
    wa_bot.nav_green_dot()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()
    wa_bot.update_conv()
    #wa_bot.nav_x()

    # Delay between checking for new messages
    sleep(10)

