import random
import pygame
from pygame import mixer
from pygame.locals import *
FPS=32
BACKGROUND='D:\Wallpapers\dragon-age-game-hero-wallpaper-2.png'


# pygame.init()
# w = 300
# h = 300
# screen = pygame.display.set_mode((w, h))
# pygame.display.set_caption('Tutorialspoint Logo')
# pygame.image.load("D:\\phone storage 17112021\\Pictures\\image.jpg")
pygame.mixer.init()
pygame.mixer.music.load("D:\\New folder\\file.wav")
pygame.mixer.music.play()
# pygame.image.load("D:\\phone storage 17112021\\Pictures\\image.jpg")
# f=open("D:\phone storage 17112021\Pictures\image_2021-07-12_13-53-25.jpg","rb")
# f.read
# f.close()
# def speak(text):
    # engine=pyttsx3.init('sapi5')
    # engine.setProperty('rate',120)
    # engine.setProperty('volume',1.0)
    # engine.say(text)
    # engine.runAndWait()


def game(plr_choice,comp, you):
    # playsound("D:\\New folder\\positions.mp3",False)
    if plr_choice==1:
        b=1
    elif plr_choice==2:
        b=2
    else:
        return None
        
    if (comp+you)%2==0:
        result2=1
    else:
        result2=2

    if b==result2 and b==1:
        return 'even'
    elif b!=result2 and b==1:
        return 'lost1'
    elif b!=result2 and b==2:
        return 'lost2'
    elif b==result2 and b==2:
        return 'odd'
if __name__=='__main__':
    try:
        plr_choice=int(input('select odd or even: press 1 for even 2 for odd: '))
    except Exception as error:
        print('The choice you have entered is not acceptable.\nPlease either enter a number or press q to exit')
        n=input()
        if n=='q':
            exit()
    print("comp has chosen, choose wisely or you lose".upper())
    comp=random.randint(1,9)
    try:
        you=int(input('enter a number: '))
    except Exception as error:
        print('The choice you have entered is not acceptable.\nPlease either enter a number or press q to exit')
        n=input()
        if n=='q':
            exit()
    
    a=game(plr_choice,comp,you)
    if a==None:
        print('not a valid choice, you have to chose from 1 or 2 i.e even or odd')
    elif a=='even':
        print(f'''comp chose={comp}\nits {a} you won!''')
    elif a=='lost1':
        print(f'''comp chose={comp}\nits odd you lose!''')
    elif a=='lost2':
        print(f'''comp chose={comp}\nits even you lose!''')
    else:
        print(f'''comp chose={comp}\nits {a} you won!''')    
