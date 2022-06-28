import sys
import pygame

import button
import env

def starting_screen(screen):
    for x in range(env.width // env.grass_img.get_width() + 1):
        for y in range(env.height // env.grass_img.get_height() + 1):
            screen.blit(env.grass_img, (x * 100, y * 100))

    game_title = env.font.render('Starting Screen', True, env.WHITE)

    screen.blit(game_title, (env.width // 2 - game_title.get_width() // 2, 150))

    play_button = button.Button('Play', env.RED, env.font, env.width, env.height, None, 350,
                                centered_x=True)
    exit_button = button.Button('Exit', env.WHITE, env.font, env.width, env.height, None, 400,
                                centered_x=True)

    play_button.display(screen)
    exit_button.display(screen)

    pygame.display.update()

    while True:

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = button.Button('Play', env.RED, env.font, env.width, env.height, None, 350,
                                        centered_x=True)
        else:
            play_button = button.Button('Play', env.WHITE, env.font, env.width, env.height, None, 350,
                                        centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = button.Button('Exit', env.RED, env.font, env.width, env.height, None, 400,
                                        centered_x=True)
        else:
            exit_button = button.Button('Exit', env.WHITE, env.font, env.width, env.height, None, 400,
                                        centered_x=True)

        play_button.display(screen)
        exit_button.display(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                break
            if exit_button.check_click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit(1)


def choose(screen):
    for x in range(env.width // env.grass_img.get_width() + 1):
        for y in range(env.height // env.grass_img.get_height() + 1):
            screen.blit(env.grass_img, (x * 100, y * 100))

    game_title = env.font.render('difficulty', True, env.WHITE)

    screen.blit(game_title, (env.width // 2 - game_title.get_width() // 2, 150))

    easy_button = button.Button('Easy', env.WHITE, env.font, env.width, env.height, 160, 300,
                                centered_x=False)
    medium_button = button.Button('Medium', env.WHITE, env.font, env.width, env.height, 280, 300,
                                  centered_x=False)
    hard_button = button.Button('Hard', env.WHITE, env.font, env.width, env.height, 450, 300,
                                centered_x=False)

    easy_button.display(screen)
    medium_button.display(screen)
    hard_button.display(screen)

    pygame.display.update()

    while True:
        if easy_button.check_click(pygame.mouse.get_pos()):
            easy_button = button.Button('Easy', env.RED, env.font, env.width, env.height, 160, 300,
                                        centered_x=False)
        else:
            easy_button = button.Button('Easy', env.WHITE, env.font, env.width, env.height, 160, 300,
                                        centered_x=False)

        if medium_button.check_click(pygame.mouse.get_pos()):
            medium_button = button.Button('Medium', env.RED, env.font, env.width, env.height, 280, 300,
                                          centered_x=False)
        else:
            medium_button = button.Button('Medium', env.WHITE, env.font, env.width, env.height, 280, 300,
                                          centered_x=False)

        if hard_button.check_click(pygame.mouse.get_pos()):
            hard_button = button.Button('Hard', env.RED, env.font, env.width, env.height, 450, 300,
                                        centered_x=False)
        else:
            hard_button = button.Button('Hard', env.WHITE, env.font, env.width, env.height, 450, 300,
                                        centered_x=False)

        easy_button.display(screen)
        medium_button.display(screen)
        hard_button.display(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if easy_button.check_click(pygame.mouse.get_pos()):
                env.badtime2 = 11
                env.blood_min = 5
                env.blood_max = 10
                break
            if medium_button.check_click(pygame.mouse.get_pos()):
                env.badtime2 = 23
                env.blood_min = 7
                env.blood_max = 15
                break
            if hard_button.check_click(pygame.mouse.get_pos()):
                env.badtime2 = 35
                env.blood_min = 13
                env.blood_max = 20
                break





def UI(screen, healthvalue):
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000 - pygame.time.get_ticks()) // 60000) + ":" +
                               str((90000 - pygame.time.get_ticks()) // 1000 % 60).zfill(2),
                               True,
                               (0, 0, 0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635, 5]
    screen.blit(survivedtext, textRect)
    screen.blit(env.healthbar_img, (5, 5))
    for health1 in range(healthvalue):
        screen.blit(env.health_img, (health1 + 8, 8))
