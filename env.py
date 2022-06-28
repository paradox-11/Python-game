import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
width, height = 640, 480

healthbar_img = pygame.image.load("../resources/images/healthbar.png")
health_img = pygame.image.load("../resources/images/health.png")
grass_img = pygame.image.load("../resources/images/grass.png")
rabbit_img = pygame.image.load("../resources/images/dude2.png")
castle_img = pygame.image.load("../resources/images/castle.png")
arrow_img = pygame.image.load("../resources/images/bullet.png")
badguy_img = pygame.image.load("../resources/images/badguy.png")
gameover_img = pygame.image.load("../resources/images/gameover.png")
youwin_img = pygame.image.load("../resources/images/youwin.png")

pygame.font.init()
font_addr = pygame.font.get_default_font()
font = pygame.font.Font(font_addr, 36)

# 难度
badtime2 = 11
blood_min = 5
blood_max = 20
