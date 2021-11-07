# This is a sample Python script.
import pygame
import math

# initialize pygame
pygame.init()

# set the game window dimensions
_screenWidth = 800
_screenHeight = 600

# creating the game window
_screen = pygame.display.set_mode((_screenWidth, _screenHeight))
pygame.display.set_caption('Castle Rush')

clock = pygame.time.Clock()
_fps = 60

# loading images
_bg = pygame.image.load('img/spacebgClone.png').convert_alpha()
# castle
_castleToDefend = pygame.image.load('img/castle2.png').convert_alpha()
# bullet
_bullet = pygame.image.load('img/bullet.png').convert_alpha()
_b_w = _bullet.get_width()
_b_h = _bullet.get_height()
_bullet = pygame.transform.scale(_bullet, (int(_b_w * 0.075)), (int(_b_h * 0.075)))

# define colors
_WHITE = (255, 255, 255)


# castle class
# this is a python constructor notated with the class keyword
class Castle():
    def __init__(self, _image, _x, _y, _scale):
        self._health = 1000
        self._maxHealth = self._health
        self.fired = False

        _width = _image.get_width()
        _height = _image.get_height()

        self._image = pygame.transform.scale(_image, (int(_width * _scale), int(_height * _scale)))
        self.rect = self._image.get_rect()

        self.rect.x = _x
        self.rect.y = _y

    def Shoot(self):
        # defining a starting position from which to aim the castle's gun
        _pos = pygame.mouse.get_pos()
        _x_dist = _pos[0] - self.rect.midleft[0]
        _y_dist = -(_pos[1] - self.rect.midleft[1])
        # apparently this has something to do with trigonometry
        self.angle = math.degrees(math.atan2(_y_dist, _x_dist))
        if pygame.mouse.get_pressed()[0] and self.fired == False:
            self.fired = True
            _thisBullet = Bullet(_bullet, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            _bulletGroup.add(_thisBullet)
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False

    def Draw(self):
        self.image = self._image

        _screen.blit(self.image, self.rect)


# define the bullet class
# the instance of this class uses the sprite class. it has its own render method so no need to use .blit
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, _x, _y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y
        self.angle = math.radians(angle)
        self.speed = 10
        # calculate the vertical and horizontal speeds based on the angle
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)

    def update(self):
        # check if bullet has left the screen so we can destroy it and free up memory
        if self.rect.right < 0 or self.rect.left > _screenWidth or self.rect.bottom < 0 or self.rect.top > _screenHeight:
            # unique to the sprite class
            self.kill()

        # move the bullet
        self.rect.x += self.dx
        self.rect.y += self.dy


# create instance of the castle class
_castle = Castle(_castleToDefend, _screenWidth - 250, _screenHeight - 250, 0.5)

# create groups
_bulletGroup = pygame.sprite.Group()

# setting the game loop
run = True
while run:
    clock.tick(_fps)

    # displaying the bg image during the game loop
    _screen.blit(_bg, (0, 0))

    # displaying castle object during game loop
    _castle.Draw()
    _castle.Shoot()
    _bulletGroup.draw(_screen)
    _bulletGroup.update()

    # initialize an event handler
    for event in pygame.event.get():
        # exit if we hit the x in the top right of the window
        if event.type == pygame.QUIT:
            run = False

    # updating screen display
    pygame.display.update()

pygame.quit()
