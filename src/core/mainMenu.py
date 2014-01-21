'''

@author: DannyUfonek

this package should deal with the main menu -> load, create, and do anything that is required
'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from menuButton import menuButton

buttons = pygame.sprite.Group()

def start(screen):
    
    pygame.init()
 
    clock = GAME_CLOCK   
    #create all the buttons
    button1 = menuButton()
    button1.text = "Play"    
    button1.__init__()
    button1.rect.x  = (100)
    button1.rect.y = (300)
    button1.add(buttons)
    textSurface1 = button1.button_font.render(button1.text, True, BLACK)
    screen.blit(textSurface1, (button1.rect.x, button1.rect.y))
    
    button2 = menuButton()
    button2.text = "Options"
    button2.__init__()
    button2.rect.x  = (100)
    button2.rect.y = (200)
    button2.add(buttons)
    textSurface2 = button2.button_font.render(button2.text, True, BLACK)
    screen.blit(textSurface2, (button2.rect.x, button2.rect.y))
    
    button3 = menuButton()
    button3.text = "Extras"
    button3.__init__()
    button3.rect.x  = (150)
    button3.rect.y = (100)
    button3.add(buttons)
    textSurface3 = button3.button_font.render(button3.text, True, BLACK)
    screen.blit(textSurface3, (button3.rect.x, button3.rect.y))
    
    # draw them on screen and update
    buttons.draw(screen)

    pygame.display.flip()
    
    print ("buttons created and drawn on screen")
    
    
    # Main Menu event loop
    menuRunning = True
    
    while menuRunning:
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("quitting")
                menuRunning = False
            if event.type == pl.MOUSEBUTTONDOWN:
                buttons.update(event)
                buttons.draw(screen)
                pygame.display.flip()
            if event.type == pl.MOUSEMOTION:
                buttons.update(event)
                buttons.draw(screen)
                pygame.display.flip()
        clock.tick(30)
        #we update twice, so that the button doesn't freeze after pressing           
        buttons.update(event)
        buttons.draw(screen)
        pygame.display.flip()
    
''' 
def updateButtons(event, screen):
    """Method for updating buttons externally"""
    buttons.update(event)
    buttons.draw(screen)
#    pygame.display.flip()
'''        

