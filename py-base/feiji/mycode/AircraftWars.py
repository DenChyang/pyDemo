# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time

def key_board_event():
    for event in pygame.event.get():
        pass

def main():
    # 创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 导入图片
    background = pygame.image.load("./source/background.png")

    # 创建一个飞机图片
    hero = pygame.image.load("./source/hero1.png")

    # 把图片放入背景中
    while True:
        screen.blit(background,(0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                # 检测按键
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                elif event.key == K_SPACE:
                    print("space")


        pygame.display.update()

        # 性能调整
        time.sleep(0.1)

if __name__ == '__main__':
    main()