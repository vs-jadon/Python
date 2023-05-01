# # Healthy_programmer
# # Prepare a program to give reminder to a programmer working
# # from 9AM to 5PM
# # by giving reminder to drink water total 3.5,
# # reminder of eye exercise in every 30 minutes
# # reminder of physical exercise in every 45 minutes
# #? 5 minutes to complete task
import time
from datetime import datetime
from pygame import mixer

def healthy_programmer ():

    def music():
        # Instantiate mixer
        mixer.init()
        mixer.music.load("D:\Virtual\Drink Water It Will You - English Dialogue.mp3")
        print("music started playing....")
        # Set preferred volume
        mixer.music.set_volume(0.8)
        # Infinite loop
        while (True):
            mixer.music.play(-1)
            print("------------------------------------------------------------------------------------")
            p = input("Press 'p' to pause")
            if p == 'p':
                mixer.music.pause()
                break
    def logger (string):
        with open ("log_book.txt","a") as book:
            book.write(f"I {string} at {datetime.now()}\n")

    in_water = time.time()
    in_eye = time.time()
    in_phy_exercise = time.time()

    while (True):
        if time.time() - in_water > 3:
            print("Drink Water")
            music()
            in_water = 0
            msg = input("Log: ")
            logger(msg)

        if time.time() - in_eye > 10:
            print("Time for Eye Exercise")
            music()
            in_eye = 0
            msg = input("Log: ")
            logger(msg)

        if time.time() - in_phy_exercise > 15 :
            print("Time for Physical Exercise")
            music()
            in_eye = 0
            msg = input("Log: ")
            logger(msg)

healthy_programmer()

#
#
# def healthy_programmer():
#         while (True):
#
#             timerr = time.time()
#             if timerr - time.time() == 3:
#                 # Instantiate mixer
#                 mixer.init()
#                 mixer.music.load("D:\Virtual\Drink Water It Will You - English Dialogue.mp3")
#                 print("music started playing....")
#                 # Set preferred volume
#                 mixer.music.set_volume(0.1)
#                 # Infinite loop
#                 while (True):
#                     mixer.music.play(-1)
#                     print("------------------------------------------------------------------------------------")
#                     p = input("Press 'p' to pause")
#                     if p == 'p':
#                         mixer.music.pause()
#                         break
#
#             if timerr - time.time() == 5:
#                 # Instantiate mixer
#                 mixer.init()
#                 mixer.music.load("D:\Virtual\Drink Water It Will You - English Dialogue.mp3")
#                 print("music started playing....")
#                 # Set preferred volume
#                 mixer.music.set_volume(0.1)
#                 # Infinite loop
#                 while (True):
#                     mixer.music.play(-1)
#                     print("------------------------------------------------------------------------------------")
#                     p = input("Press 'p' to pause")
#                     if p == 'p':
#                         mixer.music.pause()
#                         break
#
#             if timerr - time.time() == 8:
#                 # Instantiate mixer
#                 mixer.init()
#                 mixer.music.load("D:\Virtual\Drink Water It Will You - English Dialogue.mp3")
#                 print("music started playing....")
#                 # Set preferred volume
#                 mixer.music.set_volume(0.1)
#                 # Infinite loop
#                 while (True):
#                     mixer.music.play(-1)
#                     print("------------------------------------------------------------------------------------")
#                     p = input("Press 'p' to pause")
#                     if p == 'p':
#                         mixer.music.pause()
#                         break
#
#
#
