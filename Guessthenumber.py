import random
import pygame
from pygame import mixer
pygame.mixer.init()
pygame.mixer.music.load("D:\\New folder\\file.wav")
pygame.mixer.music.play()
def savescore(e):
    with open('highscore.txt') as f:
        hi_score=f.read()
# '''int(hi_score)
# g=hi_score.isdigit() to check if string is empty or not
# print(g)'''
    if e<int(hi_score):
        with open('highscore.txt','w') as f:
            f.write(str(e))
    elif e=='':
        with open('highscore.txt','w') as f:
            f.write(str(e))
        return True
    else:
        return False
if __name__=="__main":
    print("computer have guessed a number".upper())
    try:
        n=int(input('enter what you think is the number: '))
    except Exception as f:
        print("The choice you have entered is not acceptable.\nPlease either enter a number or press q to exit")
        n=input()
        if n=='q':
            exit()
    n=int(n)
    i=0
    e=1
    comp=random.randint(0,50)
    while comp!=n:
        if n<comp:
            print(f'''NOPE!!! higher then this''')
            try:
                n=int(input("enter again: "))
            except Exception as f:
                print("The choice you have entered is not acceptable.\nPlease either enter a number or press q to exit")
                n=input()
                if n=='q':
                    exit()
            n=int(n)
        elif n>comp:
            print(f'''NOPE!!! lower then this''')
            try:
                n=int(input("enter again: "))
            except Exception as f:
                print("The choice you have entered is not acceptable.\nPlease either enter a number or press q to exit")
                n=input()
                if n=='q':
                    exit()
                n=int(n)
        e=e+1
        
    
    score=savescore(e)
    if score==True:
        print(f'''congratulations you got it right it took you {e} times, its a new highscore''')
    elif score==False:
        print(f'''congratulations you got it right it took you {e} times''')
    
    
    print('thanks for playing'.upper())
    