'''

@author: DannyUfonek

handles controls changing and assigning them to events
'''
import pygame
import pygame.locals as pl
import collections
import os
import core.constants
from core.constants import *

#for translating and reassigning controls

class settingsHandler(object):
    
    settingsFont = pygame.font.Font(MAIN_MENU_FONT_PATH, 25)
    settingDict = collections.OrderedDict()
    _Number2Name = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT', 'PAUSE', 'ATTACK', 'MUSIC_VOLUME', 'SOUND_VOLUME']
    _Name2Text = {'MOVE_UP':'Up', 'MOVE_DOWN':'Down', 'MOVE_LEFT':'Left', 'MOVE_RIGHT':'Right', 'PAUSE':'Pause', 'ATTACK':'Attack', 'MUSIC_VOLUME':'Music Volume', 'SOUND_VOLUME':'Sound Volume'}
    
    def loadSettings(self):
        '''
        load existing settings file
        '''
        #readdict = {}
        with open(SETTINGS_PATH) as source:
            
            for line in source:
                #load the key and value from each line (strip is there to remove \n)
                (key, val) = line.strip().split(";")
                self.settingDict[key] = val
                
            #self.settingDict = collections.OrderedDict(readdict)
        
        print(self.settingDict)
        print("settings loaded from file and written up to constants:")
        
        for setting in self.settingDict:
            if self.settingDict[setting].startswith('K_'):
                #assign value from dictionary to constants
                x = pl.__dict__[self.settingDict[setting]]
                core.constants._ALLOWED_KEYS.append(x)
            else:
                #assign other settings from dictionary to constants
                core.constants._SETTINGS[setting] = self.settingDict[setting]
        print("allowed keys: \n {0}".format(core.constants._ALLOWED_KEYS))
        print("settings: \n {0}".format(core.constants._SETTINGS))
            
    def setSetting(self, settingNumber, settingValue = None):
        '''
        replace the key/value in dictionary and in constants
        see constants for reference which number is which control
        '''
        if settingValue == None:
            waitingforinput = True
            while waitingforinput:
                event = pygame.event.wait()
                if event.type == pl.KEYDOWN:
                    print(event.key)
                    # if a key is pressed, assign it to the control in constants
                    core.constants._ALLOWED_KEYS[settingNumber] = event.key
                    # convert its integer to string form
                    # get the setting we're saving to
                    # then save it to dictionary
                    self.settingDict[self._Number2Name[settingNumber]] = "K_{}".format(pygame.key.name(event.key))
                else:
                    pass
        else:
            # change value of setting in constants -> this is a dict so we have to convert as well
            core.constants._SETTINGS[self._Number2Name[settingNumber]] = settingValue
            # convert its integer to string form
            # get the setting we're saving to
            # then save it to dictionary
            self.settingDict[self._Number2Name[settingNumber]] = settingValue
        
    def drawSetting(self, settingNumber = "EMPTY", colour = FULL_RED):
        '''
        draw an existing setting into a surface
        drawSetting(setting) --> Surface
        '''
        if settingNumber == "EMPTY":
            image = self.settingsFont.render("_", True, colour)
        else:
            settingName = self._Number2Name[settingNumber]
            text = self.settingDict[settingName]
            if text.startswith("K_"):
                text = text.partition("K_")[2]
            image = self.settingsFont.render(text, True, colour)
        
        return image
        
    def saveSettings(self):
        '''
        save the existing settingDict to file
        saveSettings() --> None
        '''
        with open(SETTINGS_PATH, 'w') as output:
            for setting in self.settingDict:
                #write out the dictionary
                value = self.settingDict[setting]
                output.write('{0};{1}\n'.format(setting, value))
            print("saved settings to {}".format(SETTINGS_PATH))
    
    