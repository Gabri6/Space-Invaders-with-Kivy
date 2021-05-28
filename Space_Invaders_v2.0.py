#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Fri 30 Apr 2021 10:33:52 CET
# Author: Gabriel Lucas
# Description:
# Python Version 3.9
#Last modified: Mon 03 May 2021 11:00:05 CET
#By: Gabriel Lucas


import random
from kivy.app import App
from kivy.config import Config 
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.logger import Logger

Playerl = []
Scorel = []

try:
    with open('répertoire.txt', 'r') as f:
        for line in f:
            n,t = [elt for elt in line.split(";")]
            Playerl.append(n), Scorel.append(t)
    print('répertoire chargé')

except:
    print('pas encore de répertoire')

class MenuScreen(Screen):
    def build(self):
        self.name='Menu'

        self.add_widget(Image(source='KsVElpX-space-invaders-wallpaper.png',allow_stretch=True,keep_ratio=False))

        Menu_Layout = BoxLayout(padding=100,spacing=10,orientation='vertical')


#        self.tblScore=
#        PlayerName=Label(text='New Player')
        self.entry=TextInput(text='New Player',
            font_size=Window.size[0]*0.05,
            height=2,
            multiline=False,
            foreground_color=(1,1,1,1),
            background_color=(0,0,0,0))
        #self.entry.bind(on_text_validate=lambda *a:appName2(self.entry.text))
        #entry.bind(text=self.PlayerName.setter('text'))

        self.Bouton_Exit=Button(text='Exit')
        self.Bouton_Exit.font_size=Window.size[0]*0.05
        self.Bouton_Exit.background_color=[0,0,0,0.2]
        self.Bouton_Exit.bind(on_press=self.Vers_Exit)

        self.Bouton_Jeu=Button(text='Play !')
        self.Bouton_Jeu.font_size=Window.size[0]*0.05
        self.Bouton_Jeu.background_color=[0,0,0,0.2]
        self.Bouton_Jeu.bind(on_press=lambda *a:appName2(self.entry.text),on_release=self.Vers_Game)

        Menu_Layout.add_widget(self.Bouton_Jeu)
        Menu_Layout.add_widget(self.Bouton_Exit)
        Menu_Layout.add_widget(self.entry)



        self.add_widget(Menu_Layout)


    def Vers_Game(self,instance):
        Game=GameScreen()
        Game.build()
        sm.add_widget(Game)
        sm.current='Game'
    def Vers_Exit(self,instance):
        SpaceApp().stop()
class GameScreen(Screen):
    def build(self):
        self.name='Game'
        Game_Layout=SpaceGame()
        #Game_Layout.debut()
        self.add_widget(Game_Layout)
class PauseScreen(Screen):
    def build(self):
        self.name='Pause'

        self.add_widget(Image(source='KsVElpX-space-invaders-wallpaper.png',allow_stretch=True,keep_ratio=False))

        Pause_Layout = BoxLayout(padding=100,spacing=10,orientation='vertical')

        self.Bouton_Exit_P=Button(text='Exit')
        self.Bouton_Exit_P.font_size=Window.size[0]*0.05
        self.Bouton_Exit_P.background_color=[0,0,0,0.2]
        self.Bouton_Exit_P.bind(on_press=self.Vers_Exit_P)

        self.Bouton_Resume_P=Button(text='Resume')
        self.Bouton_Resume_P.font_size=Window.size[0]*0.05
        self.Bouton_Resume_P.background_color=[0,0,0,0.2]
        self.Bouton_Resume_P.bind(on_press=self.Vers_Game_P)

        self.Score=Label(text='root.tank.score')

        Pause_Layout.add_widget(self.Bouton_Resume_P)
        Pause_Layout.add_widget(self.Bouton_Exit_P)
        Pause_Layout.add_widget(self.Score)



        self.add_widget(Pause_Layout)

    def Vers_Game_P(self,instance):
        try:
            Game=GameScreen()
            #Game.build()
            sm.add_widget(Game)
            sm.current='Game'
        except:
            TROLL=TROLLScreen()
            TROLL.build()
            sm.add_widget(TROLL)
            sm.current='TROLL'
    def Vers_Exit_P(self,instance):
        SpaceApp().stop()


class TROLLScreen(Screen):
    def build(self):
        self.name='TROLL'

        self.add_widget(Image(source='KsVElpX-space-invaders-wallpaper.png',allow_stretch=True,keep_ratio=False))

        TROLL_Layout = BoxLayout(padding=100,spacing=10,orientation='vertical')
        self.Score=Label(text="   Who is dumb enough to put\nthe game in pause when it hasn't\n        even started !!")
        self.Score.font_size=Window.size[0]*0.05
        self.Bouton_Exit_T=Button(text='Exit')
        self.Bouton_Exit_T.font_size=Window.size[0]*0.05
        self.Bouton_Exit_T.background_color=[0,0,0,0.2]
        self.Bouton_Exit_T.bind(on_press=self.Vers_Exit_T)
        TROLL_Layout.add_widget(self.Score)
        TROLL_Layout.add_widget(self.Bouton_Exit_T)
        self.add_widget(TROLL_Layout)
    def Vers_Exit_T(self,instance):
        SpaceApp().stop()


def appName2(message):
    with open('répertoire.txt','a') as f:
        f.write(f'{message};')
    print(message)


with open("sauvegarde.kv", "r")as s:
    with open("Space.kv", "w") as f:
        f.write(s.read())




class SpaceTank(Widget):
    pass
'''
######################################################

class SpaceFleet(Widget):
    def __init__(self,canvas):
        self.rows = 2
        self.cols = 2
        self.dy=-10
        self.x =100
        self.y=Window.size[1]-100
        self.canvas = canvas
        self.alien=[]
        self.width = self.cols * 50
        self.height = self.rows * 50
    def create_fleet(self):
        for i in range(self.cols):
            for j in range(self.rows):
                x = (self.width - self.width) / 2 + (i + 1) * 50
                y = self.height - ((j + 1) * 50)
                self.add_widget(SpaceAliens(self.canvas,x,y))
                self.add_alien(aliens)
    def move(self):
                #On recalcule les positions:
        self.y=self.y+self.dy
        #On teste la fin de la chute:
        if self.y<=0-self.size[1]:
            #Repositionnement aleatoire en haut:
            self.y=Window.size[1]
            self.x=random.randint(0,int(Window.size[0]-self.size[0]))
        for a in self.alien:
            a.center_y+=self.dy
    def add_alien(self, aliens):
        self.alien.append(aliens)
        ship.fleet = self




class SpaceAliens(Widget):
    def __init__(self,canvas,x,y):
        self.canvas = canvas
        self.size=(50,50)
        self.dy=-10
        self.x =x
        self.y=y
        #Image
        with self.canvas:
            self.dessin = Rectangle(source='invader.jpg',size=self.size, pos=self.pos)
        #Detection des mouvements:
        self.bind(pos=self.update_canvas)
 
    def update_canvas(self, *args):#Image pos
        self.dessin.pos = self.pos

    def move(self,y=0,x=0):
        #positions:
        self.x+=x
        self.y+=y
   
    def prise(self):#Changement d'image pour le succes:
        self.dy=0#On stoppe la chute
        #Position au dessus du panier pour stopper la collision:
        self.y=Window.size[1]*0.2  
        Clock.schedule_once(self.prise_fin, 0.5)





class Jeu(FloatLayout):
    def debut(self):
        self.size=Window.size
        self.alien=SpaceFleet(self.canvas)
        self.add_fleet()
        self.add_widget(SpaceGame())
        Clock.schedule_interval(self.update_displacement, 50.0/100.0)
    def update_displacement(self,dt):#Chute des lapins et tests de collisions
        self.alien.move()
    def add_fleet(self):
        self.alien.create_fleet()
'''
class Fleet(Widget):
    last_move_direction = NumericProperty(1)
    move_direction = NumericProperty(0)

    MOVE_TIME = 0.5
    MOVE_STEP = 10

    def __init__(self, **kwargs):
        self.rows = kwargs.pop('rows', 0)
        self.cols = kwargs.pop('cols', 0)

        super(Fleet, self).__init__(**kwargs)

        self.width = self.cols * Invader().width
        self.height = self.rows * Invader().height

        self.last_update = None
        self.elapsed = 0
        self.ships = []
        self.move_direction = 1

    def create_fleet(self):
        for i in range(self.cols):
            for j in range(self.rows):
                invader = Invader()
                invader.x = (self.parent.width - self.width) / 2 + (i + 1) * invader.width
                invader.y = self.parent.height - ((j + 1) * invader.height)

                self.add_ship(invader)

    def add_ship(self, ship):
        self.ships.append(ship)
        ship.fleet = self

    def update(self, dt):
        self.elapsed += dt

        if self.elapsed > self.MOVE_TIME or self.last_update is None:
            #Logger.debug('move_dir=%d, last_dir=%d, x=%d, y=%d, height=%d, width=%d' % (self.move_direction, self.last_move_direction, self.x, self.y, self.height, self.width))

            # Move based on current direction.
            if self.move_direction == 0:
                self.center_y -= self.MOVE_STEP
                for s in self.ships:
                    s.center_y -= self.MOVE_STEP

                # After moving down switch back to moving horizontally.
                self.last_move_direction, self.move_direction = self.move_direction, -self.last_move_direction

            else:
                # Move left or right.
                self.center_x += self.move_direction * self.MOVE_STEP
                for s in self.ships:
                    s.center_x += self.move_direction * self.MOVE_STEP

                # Reset position and direction if out of bounds.
                if self.x <= 0:
                    self.last_move_direction, self.move_direction = self.move_direction, 0

                elif self.x + self.width >= self.parent.width:
                    self.last_move_direction, self.move_direction = self.move_direction, 0

            self.last_update, self.elapsed = self.elapsed, 0
        def update(self, dt):
            self.fleet.update(dt)

            for e in self._entities[:]:
                status = e.update(dt)
                if not status or e.collision_detected:
                    self._remove_entity(e)

        return True




class Invader(Widget):
    image = StringProperty('space_invaders_icon.jpg')
    last_move_direction = NumericProperty(0)
    move_direction = NumericProperty(0)

    MOVE_TIME = 0.5
    MOVE_STEP = 10

    def __init__(self, **kwargs):
        super(Invader, self).__init__(**kwargs)

        self.fleet = None
        self.last_update = None
        self.elapsed = 0
        self.collision_detected = False

    def update(self, dt):
        self.elapsed += dt

        # NOTE: Only move if not a part of a fleet.  Let the fleet control movement normally.
        if not self.fleet and (self.elapsed > self.MOVE_TIME or self.last_update is None):
            # Move based on current direction.
            if self.move_direction == 0:
                self.center_y -= self.MOVE_STEP

                # After moving down switch back to moving horizontally.
                self.last_move_direction, self.move_direction = self.move_direction, -self.last_move_direction

            else:
                # Move left or right.
                self.center_x += self.move_direction * self.MOVE_STEP

                # Reset position and direction if out of bounds.
                if self.x <= 0:
                    self.last_move_direction, self.move_direction = self.move_direction, 0

                elif self.x + self.width >= self.parent.width:
                    self.last_move_direction, self.move_direction = self.move_direction, 0
            
            self.last_update, self.elapsed = self.elapsed, 0

        return True
    
#####################################################

bullets=[]
class SpaceBullet(Widget):
    last_move_direction = NumericProperty(0)
    move_direction = NumericProperty(0)

    MOVE_TIME = 1.0/60.0
    MOVE_STEP = 10

    def __init__(self, **kwargs):
        super(SpaceBullet, self).__init__(**kwargs)

        self.fleet = None
        self.last_update = None
        self.elapsed = 0
        self.collision_detected = False

    def update(self, dt):
        self.elapsed += dt

        # NOTE: Only move if not a part of a fleet.  Let the fleet control movement normally.
        if not self.fleet and (self.elapsed > self.MOVE_TIME or self.last_update is None):
            # Move based on current direction.
            if self.move_direction == 0:
                self.center_y += self.MOVE_STEP

                # After moving down switch back to moving horizontally.
                self.last_move_direction, self.move_direction = self.move_direction, -self.last_move_direction

            else:
                # Move left or right.
                self.center_x += self.move_direction * self.MOVE_STEP

                # Reset position and direction if out of bounds.
                if self.x <= 0:
                    self.last_move_direction, self.move_direction = self.move_direction, 0

                elif self.x + self.width >= self.parent.width:
                    self.last_move_direction, self.move_direction = self.move_direction, 0
            
            self.last_update, self.elapsed = self.elapsed, 0

        return True

class SpaceBunkerbits(Widget):
    life = NumericProperty(4)
    def bunker_hit(self, bullet):
        if self.collide_widget(bullet):
                self.life -= 1
                if self.life == 0:
                    pass                     #à compléter   

class SpaceBunker(Widget):
    pass
    '''
    def __init__(self, **kwargs):
        self.entities = []
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x - 30,SpaceBunker.center_y - 20))
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x - 30,SpaceBunker.center_y))
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x - 10,SpaceBunker.center_y))
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x - 10,SpaceBunker.center_y + 20))
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x + 10,SpaceBunker.center_y))
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x + 10,SpaceBunker.center_y + 20))
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x + 30,SpaceBunker.center_y - 20))
        self.add_widget(SpaceBunkerbits,pos=(SpaceBunker.center_x + 30,SpaceBunker.center_y))
'''
class SpaceGame(Widget):
    def __init__(self, **kwargs):
        super(SpaceGame, self).__init__(**kwargs)
        self._entities = []
        self.size = (800, 600)
        self._init_fleet()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        Clock.schedule_interval(self.update, 1.0 / 60.0)


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    def update(self, dt):
        '''
        self.bunker1.square1.bunker_hit(self.e for e in self._entities)
        self.bunker1.square2.bunker_hit(self.e for e in self._entities)
        self.bunker1.square3.bunker_hit(self.e for e in self._entities)
        self.bunker1.square4.bunker_hit(self.e for e in self._entities)
        self.bunker1.square5.bunker_hit(self.e for e in self._entities)
        self.bunker1.square6.bunker_hit(self.e for e in self._entities)
        self.bunker1.square7.bunker_hit(self.e for e in self._entities)
        self.bunker1.square8.bunker_hit(self.e for e in self._entities)
        '''
        self.fleet.update(dt)
        for e in self._entities[:]:
            status = e.update(dt)
            if not status or e.collision_detected:
                self._remove_entity(e)
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'right':
            if self.tank.center_x < self.width:    
                self.tank.center_x += 10
        elif keycode[1] == 'left':
            if self.tank.center_x > 0:
                self.tank.center_x -= 10
        if keycode[1] == 'left'+'spacebar':
            if self.tank.center_x > 0:
                self.tank.center_x -= 10
            bullet = SpaceBullet()
            bullet.center = (self.tank.center_x, self.tank.center_y+5)
            self._add_entity(bullet)
        if keycode[1] == 'spacebar':
            bullet = SpaceBullet()
            bullet.center = (self.tank.center_x, self.tank.center_y+5)
            self._add_entity(bullet)
        if keycode[1] == 'm':
            bullet = SpaceBullet()
            bullet.center = (self.tank.center_x, self.tank.center_y+5)
            self._add_entity(bullet)
        if keycode[1] in ('p', 'escape'):
            Pause=PauseScreen()
            Pause.build()
            sm.add_widget(Pause)
            sm.current='Pause'
            
        elif keycode[1] == 'z':
            invader = Invader()
            invader.center = (random.randint(0, self.width), random.randint(self.height * 0.66, self.height))

            self._add_entity(invader)
    def _init_fleet(self):
        self.fleet = Fleet(rows=5, cols=10)
        self.fleet.pos = ((self.width - self.fleet.width) / 2 + 50, 0)
        self.add_widget(self.fleet)

        self.fleet.create_fleet()
        for s in self.fleet.ships:
            self._add_entity(s)

    def _add_entity(self, entity, skip_widget=False):
        self._entities.append(entity)
        if not skip_widget:
            self.add_widget(entity)

    def _remove_entity(self, entity):
        self.remove_widget(entity)
        self._entities.remove(entity)
        return True






'''
class SpaceApp(App):
    def build(self):
        game = SpaceGame()
        self.title = 'Space Invaders'
        self.icon = 'space_invaders_icon.jpg'
        return game
<SpaceAliens>:
    size: 50, 50

    canvas:
        Ellipse:
            pos. self.pos
            size: self.size
            source: self.image
'''
    
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
'''
SpaceApp().run()

'''

sm = ScreenManager()

class SpaceApp(App):
    def build(self):
        game = SpaceGame()
        self.title = 'Space Invaders'
        self.icon = 'space_invaders_icon.jpg'
        Menu=MenuScreen()
        Menu.build()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        sm.add_widget(Menu)
        sm.current='Menu'
        return sm
 
if __name__ == '__main__':
    SpaceApp().run()
