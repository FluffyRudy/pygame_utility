import sys
import os
from pathlib import Path
import pygame


def main():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
    from src.map_loader.maploader import MapLoader

    map_path = Path(__file__).resolve().parent / "maps" / "map.tmx"

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    maploader = MapLoader(map_path)
    map_data = maploader.get_map_data()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))  # Clear the screen with black

        for layername, layer_data in map_data.items():
            for d in layer_data:
                try:
                    x, y, s = d
                    screen.blit(s, (x, y))
                except:
                    print(d, layername)

        pygame.display.flip()


main()
