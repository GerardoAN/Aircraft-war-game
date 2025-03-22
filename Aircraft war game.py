# Python网课学习
import pygame
import time
from pygame.locals import *

hero_x = 150
hero_y = 600
my_bullet = []


def hero_plane(screen, hero, bullet):
    global hero_x, hero_y, my_bullet
    screen.blit(hero, (hero_x, hero_y))
    for event in pygame.event.get():
        if event == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                print("您按了向上")
                hero_y -= 20
            if event.key == K_DOWN:
                print("您按了向上")
                hero_y += 20
            if event.key == K_LEFT:
                print("您按了向左")
                hero_x -= 20
            if event.key == K_RIGHT:
                print("您按了向右")
                hero_x += 20
            if event.key == K_SPACE:
                print("发射子弹")
                my_bullet.append({"x": hero_x + 20, "y": hero_y - 20})
    for i in my_bullet:
        screen.blit(bullet, (i["x"], i["y"]))
        screen.blit(bullet, (i["x"] + 20, i["y"]))
        screen.blit(bullet, (i["x"] + 40, i["y"]))
        i["y"] -= 10


enemy_x = 125
enemy_path = "LEFT"
a = pygame.image.load("./aircraft_war_material/enemy2_down1.png")
b = pygame.image.load("./aircraft_war_material/enemy2_down2.png")
c = pygame.image.load("./aircraft_war_material/enemy2_down3.png")
d = pygame.image.load("./aircraft_war_material/enemy2_down4.png")
e = pygame.image.load("./aircraft_war_material/enemy2_down5.png")
f = pygame.image.load("./aircraft_war_material/enemy2_down6.png")
blow_up = [a, b, c, d, e, f]
enemy_life = "live"
enemy_num = 0


def enemy_plane(screen, enemy):
    global enemy_x, enemy_path, enemy_num, enemy_life

    for bullet in my_bullet:
        if (bullet["x"] >= enemy_x and bullet["x"] <= enemy_x + 165) and (bullet["y"] >= 0 and bullet["y"] <= 265):
            enemy_life = "dead"

    if enemy_life == "live":
        screen.blit(enemy, (enemy_x, 10))
        if enemy_x >= 235:
            enemy_path = "LEFT"
        elif enemy_x <= 0:
            enemy_path = "RIGHT"
        if enemy_path == "LEFT":
            enemy_x -= 5
        elif enemy_path == "RIGHT":
            enemy_x += 5
    elif enemy_life == "dead":
        if enemy_num <= 5:
            screen.blit(blow_up[enemy_num], (enemy_x, 10))
            enemy_num += 1


def main():
    screen = pygame.display.set_mode((400, 800), 0, 32)

    background = pygame.image.load("./aircraft_war_material/background.png")
    hero = pygame.image.load("./aircraft_war_material/hero1.png")
    bullet = pygame.image.load("./aircraft_war_material/plane.png")
    enemy = pygame.image.load("./aircraft_war_material/enemy2.png")
    while True:
        screen.blit(background, (0, 0))
        hero_plane(screen, hero, bullet)
        enemy_plane(screen, enemy)
        pygame.display.set_caption("飞机大战")
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
