import math
import sys
import pygame
from pygame.locals import *

import button
import env

flag = 0


def key_event(acc, arrows, keys, playerpos, playerpos1):
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # 移动 wasd
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False
        # 鼠标
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_mouse = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [math.atan2(position_mouse[1] - (playerpos1[1] + 32), position_mouse[0] - (playerpos1[0] + 26)),
                 playerpos1[0] + 32,
                 playerpos1[1] + 26]
            )
    # 玩家移动
    if keys[0]:
        playerpos[1] -= 3
    elif keys[2]:
        playerpos[1] += 3
    if keys[1]:
        playerpos[0] -= 3
    elif keys[3]:
        playerpos[0] += 3


def pass_check(accuracy, exitcode, screen):
    if not exitcode:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 24
        screen.blit(env.gameover_img, (0, 0))
        screen.blit(text, textRect)
    else:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 24
        screen.blit(env.youwin_img, (0, 0))
        screen.blit(text, textRect)


    while True:
        play_button = button.Button('Replay', env.RED, env.font, env.width, env.height, 100, 350,
                                    centered_x=False)
        exit_button = button.Button('Exit', env.WHITE, env.font, env.width, env.height, 100, 400,
                                    centered_x=False)

        play_button.display(screen)
        exit_button.display(screen)

        pygame.display.update()

        while True:

            if play_button.check_click(pygame.mouse.get_pos()):
                play_button = button.Button('Replay', env.RED, env.font, env.width, env.height, 100, 350,
                                            centered_x=False)
            else:
                play_button = button.Button('Replay', env.WHITE, env.font, env.width, env.height, 100, 350,
                                            centered_x=False)

            if exit_button.check_click(pygame.mouse.get_pos()):
                exit_button = button.Button('Exit', env.RED, env.font, env.width, env.height, 100, 400,
                                            centered_x=False)
            else:
                exit_button = button.Button('Exit', env.WHITE, env.font, env.width, env.height, 100, 400,
                                            centered_x=False)

            play_button.display(screen)
            exit_button.display(screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
            if pygame.mouse.get_pressed()[0]:
                if play_button.check_click(pygame.mouse.get_pos()):
                    flag = 1
                    break
                if exit_button.check_click(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit(1)
            pass

        if flag == 1:
            break
