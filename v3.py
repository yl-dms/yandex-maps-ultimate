import os
import sys

import pygame
import requests

coord = ["37.530887", "55.703118", "0.002"]


def req(lon, lat, delta):
    api_server = "http://static-maps.yandex.ru/1.x/"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    print("req finish")
    return map_file


map_file = req(*coord)
pygame.init()
screen = pygame.display.set_mode((600, 450))
pic = pygame.image.load(map_file)
screen.blit(pic, (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP and float(coord[2]) <= 45:
                coord[2] = str(float(coord[2]) * 2)
                print("start req")
                map_file = req(*coord)
                pic = pygame.image.load(map_file)
                screen.blit(pic, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_PAGEDOWN and float(coord[2]) >= 0.002:
                coord[2] = str(float(coord[2]) / 2)
                print("start req")
                map_file = req(*coord)
                pic = pygame.image.load(map_file)
                screen.blit(pic, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_UP:
                coord[1] = str(float(coord[1]) + float(coord[2]) / 2)
                print("start req")
                map_file = req(*coord)
                pic = pygame.image.load(map_file)
                screen.blit(pic, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                coord[1] = str(float(coord[1]) - float(coord[2]) / 2)
                print("start req")
                map_file = req(*coord)
                pic = pygame.image.load(map_file)
                screen.blit(pic, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                coord[0] = str(float(coord[0]) + float(coord[2]) / 2)
                print("start req")
                map_file = req(*coord)
                pic = pygame.image.load(map_file)
                screen.blit(pic, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_LEFT:
                coord[0] = str(float(coord[0]) - float(coord[2]) / 2)
                print("start req")
                map_file = req(*coord)
                pic = pygame.image.load(map_file)
                screen.blit(pic, (0, 0))
                pygame.display.flip()
pygame.quit()

os.remove(map_file)
