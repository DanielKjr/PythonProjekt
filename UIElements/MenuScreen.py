import pygame

class Menu():

    def __init__(self):
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.my_font.render("Welcome To Frawger", False, (0,0,0))
        #self.rect = self.text_surface.get_rect()
        self.rect = pygame.Rect(0,0, 200,200)
        self.isactive = True


    def menu_update(self, dt):

        
         point = pygame.mouse.get_pos()

         collide = self.rect.collidepoint(point)
         if collide:
            print("it be colliding")
        

    
    def draw(self, screen):
        
         screen.fill((0, 150, 155))
         screen.blit(self.text_surface, (400,500))


    