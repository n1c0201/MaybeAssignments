import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('', os.sep)
                image = pygame.image.load('gardyan.jpg')
                _image_library[path] = image
        return image
 
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
done = False
is_blue = True
x = 30
y = 30
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1
        if is_blue: 
            color = (0, 128, 255)
        else: 
            color = (255, 100, 0)
        screen.fill((0,0,0))
        screen.blit(get_image('gardyan.jpg'), (x,y))

         
        pygame.display.flip()