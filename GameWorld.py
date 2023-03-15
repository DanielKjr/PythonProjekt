from msvcrt import setmode
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log
from GameObjects.Player import Player
from LogSpawnerMan import LogSpawnerMan


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class GameWorld(metaclass=Singleton):

    _gameobjects = []
    _player = []
    
    # region PROPERTIESBIATCH
    # @property
    # def gameObjects(self):
    #     return self.gameObjects

    # @gameObjects.setter
    # def gameObjects(self, value):
    #     self.gameObjects = value
    #     self._gameobjects.add(value)

    def __init__(self):
        self.logSpawnerMan = LogSpawnerMan()
        self.deltatime = 0

    @property
    def deltatime(self):
        return self.deltatime

    # endregion

    def get_gameobjects(self):
        return self._gameobjects
    
    def get_gameobject_count(self):
        return self._gameobjects.count(self)
    
    def get_player(self):
        return self._player

    def runpygame(self):
        self.__init__(self)
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("My Pygame window")
        fps = 60.0
        fpsClock = pygame.time.Clock()
        #dt = 1/fps
        self.deltatime = 1/fps

        player = Player("Sprites/Player/Player1.png")
        self._player.append(player)






        # gameloop
        while True:
            self.update(self, self.deltatime)
            self.draw(self, screen)
            #dt = fpsClock.tick(fps) / 1000.0
            self.deltatime = fpsClock.tick(fps) / 1000.0
            

            


    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for p in self.get_player(self):
            p.update(dt)
        for go in self.get_gameobjects(self):
            #removes references
            if go.toberemoved:
                self._gameobjects.remove(go)
            else:
             go.update(dt)

        if(self._gameobjects.count(GameObject) <= 8):
            self.createlogs(self)

        self.collisionCheck(self)




    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        for go in self.get_gameobjects(self):
           go.draw(screen) 
           
        for p in self.get_player(self):
            p.draw(screen)
            
        pygame.display.update()

    def createlogs(self):
        self.gwspawns = self.logSpawnerMan.checkready()
        if self.gwspawns is not 0:
            self._gameobjects.append(self.logSpawnerMan.spawnLog(self.gwspawns))
        else:
            pass


    def collisionCheck(self):
        for p in self._player:
            for go in self._gameobjects:
                if go.tag == "Log":  
                    if p.rect.colliderect(go.sprite.rect):
                     go.onCollision(p)
                     #p.onCollision(go)



if __name__ == '__main__':

    GameWorld.runpygame(GameWorld)
