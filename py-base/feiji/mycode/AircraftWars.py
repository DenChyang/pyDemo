# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time

class Base(object):
    """
    基类
    """
    def __init__(self,x,y,image_addr,screen_temp):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_addr)
        self.screen = screen_temp

class HeroPlane(Base):
    '''
    飞机类
    '''
    def __init__(self,screen_temp):
        Base.__init__(210,600,"./source/hero1.png",screen_temp)
        self.bullet_list = []
    def show_hero(self): # 显示英雄
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.show_bullet()
            bullet.move()
    def move_left(self): # 向左
        self.x -= 5
    def move_right(self): # 向右
        self.x += 5
    def move_up(self): # 向上
        self.y -= 5
    def move_down(self): # 向下
        self.y += 5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
class EnemyPlane(Base):
    '''
    敌机类
    '''
    def __init__(self,screen_temp):
        Base.__init__(210,600,"./source/hero1.png",screen_temp)
        self.x = 0
        self.y = 44
        self.image = pygame.image.load("./source/hero1.png")
        self.screen = screen_temp
        self.bullet_list = []
    def show_hero(self): # 显示英雄
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.show_bullet()
            bullet.move()
    def move_left(self): # 向左
        self.x -= 5
    def move_right(self): # 向右
        self.x += 5
    def move_up(self): # 向上
        self.y -= 5
    def move_down(self): # 向下
        self.y += 5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


class Bullet(object):
    '''
    子弹类
    '''
    def __init__(self,screen_temp,x,y):
        self.x = x + 40
        self.y = y -15
        self.image = pygame.image.load("./source/bullet.png")
        self.screen = screen_temp

    def show_bullet(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y -= 15

def key_board_event(hero_temp):
    '''
    键盘事件方法
    :param hero_temp:
    :return:
    '''
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            # 检测按键
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print("space")
                hero_temp.fire()

def main():
    '''
    主函数方法
    :return:
    '''
    # 创建窗口
    screen = pygame.display.set_mode((480, 700), 0, 32)
    # 导入图片
    background = pygame.image.load("./source/background.png")

    # 创建一个飞机图片
    hero = HeroPlane(screen)

    # 把图片放入背景中
    while True:
        screen.blit(background,(0,0))
        hero.show_hero()
        key_board_event(hero)
        pygame.display.update()
        # 性能调整
        time.sleep(0.1)

if __name__ == '__main__':
    main()