import pygame
import math
import random

import screen_interface
import events
import env


def main():
    # pygame初始化
    pygame.init()
    screen = pygame.display.set_mode((env.width, env.height))

    # 键盘按键
    keys = [False, False, False, False]
    playerpos = [100, 100]
    acc = [0, 0]  # 命中
    arrows = []  # 箭矢

    badtimer = 100
    badtimer1 = 1
    badguys = [[640, 100]]  # 敌人 列表
    healthvalue = 194

    running = True
    exitcode = False

    # 开始界面
    screen_interface.starting_screen(screen)
    #

    # 难度选择
    screen_interface.choose(screen)
    #

    while running:
        # 更新显示内容
        pygame.display.flip()

        # 初始化屏幕图片
        screen.fill(0)
        for x in range(env.width // env.grass_img.get_width() + 1):
            for y in range(env.height // env.grass_img.get_height() + 1):
                screen.blit(env.grass_img, (x * 100, y * 100))

        screen.blit(env.castle_img, (0, 30))
        screen.blit(env.castle_img, (0, 135))
        screen.blit(env.castle_img, (0, 240))
        screen.blit(env.castle_img, (0, 345))

        # 显示玩家
        position_mouse = pygame.mouse.get_pos()  # 鼠标位置
        angle = math.atan2(position_mouse[1] - (playerpos[1] + 32),
                           position_mouse[0] - (playerpos[0] + 26))  # 角度π
        playerrot = pygame.transform.rotate(env.rabbit_img,
                                            360 - angle * 57.29)  # 图片旋转
        # 从playerpos转为playerpos1，坐标转换
        playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2,
                      playerpos[1] - playerrot.get_rect().height / 2)
        screen.blit(playerrot, playerpos1)  # 显示人物
        # 显示箭矢
        for projective in arrows:
            arrow1 = pygame.transform.rotate(env.arrow_img, 360 - projective[0] * 57.29)
            screen.blit(arrow1, (projective[1], projective[2]))
        # 显示敌人
        for badguy in badguys:
            screen.blit(env.badguy_img, badguy)

        # 武器动作
        for bullet in arrows:
            index = 0
            # 为了保持单位速度，需做三角函数运算
            velx = math.cos(bullet[0]) * 10
            vely = math.sin(bullet[0]) * 10
            bullet[1] += velx
            bullet[2] += vely

            # 出界移除
            if bullet[1] < - 64 or bullet[1] > 640 or bullet[2] < - 64 or bullet[2] > 480:
                arrows.pop(index)
            index += 1

        badtimer -= 1
        if badtimer == 0:
            # 添加敌人
            badguys.append([640, random.randint(50, 365)])
            badtimer = 100 - (badtimer1 * 2)
            # 数字越小敌人越少
            if badtimer1 >= env.badtime2:
                badtimer1 = env.badtime2
            else:
                badtimer1 += 5
        index_badguy = 0
        for badguy in badguys:
            # 如果超出边界，就删除敌人
            if badguy[0] < -64:
                badguys.pop(index_badguy)
            # 敌人移速
            badguy[0] -= 2
            badrect = pygame.Rect(env.badguy_img.get_rect())
            badrect.top = badguy[1]
            badrect.left = badguy[0]

            # 敌人攻击我方
            if badrect.left < 64:
                # 受攻击掉血量
                healthvalue -= random.randint(env.blood_min, env.blood_max)
                badguys.pop(index_badguy)

            # 箭矢击中敌人动作
            index_arrow = 0
            for bullet in arrows:
                bulletrect = pygame.Rect(env.arrow_img.get_rect())
                bulletrect.left = bullet[1]
                bulletrect.top = bullet[2]
                if badrect.colliderect(bulletrect):
                    acc[0] += 1
                    badguys.pop(index_badguy)
                    arrows.pop(index_arrow)
                index_arrow += 1

        # 界面UI
        screen_interface.UI(screen, healthvalue)

        # 获取事件
        events.key_event(acc, arrows, keys, playerpos, playerpos1)

        # 游戏结束监测
        if pygame.time.get_ticks() >= 90000:
            running = False
            exitcode = True
        if healthvalue <= 0:
            running = False
            exitcode = False

        if acc[1] != 0:
            accuracy = acc[0] * 1.0 / acc[1] * 100
            accuracy = ("%.2f" % accuracy)
        else:
            accuracy = 0
        # 检测是否通关

    events.pass_check(accuracy, exitcode, screen)
    pass





if __name__ == "__main__":
    while 1:
        main()
