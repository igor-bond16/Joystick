import pygame
from pygame.local import *

pygame.init()
screen = pygame.display.set_mode((320,240))
pygame.joystick.init()
print("get_count:"+str(pygame.joystick.get_count))
if pygame.error:
    print("Joystick is not connected")
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("get_name:"+joystick.get_name)
print("get_numaxes:"+str(joystick.get_numaxes()))
print("get_numbuttons:"+str(joystick.get_numbuttons()))
print("get_numhats:"+str(joystick.get_numhats()))
myfont = pygame.font.Font(None,30)
myclock = pygame.time.Clock()

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

        if e.type == pygame.locals.JOYAXISMOTION:
            scrren.fill(WHITE)
            text = myfont.render("axis:"+str(joystick.get_axis(0))+" , "+str(joystick.get_axis(1)),True,BLACK)
            surface.blit(text,(50,100))
            pygame.display.update()
            myclock.tick(60)

pygame.quit()