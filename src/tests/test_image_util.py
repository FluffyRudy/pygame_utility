# tests/test_image_util.py

import unittest
import pygame
from pygame_utility import image_util


class TestImageUtil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        display_mode = pygame.display.set_mode((0, 0))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_load_image(self):
        # Assuming image_util.py has a function called load_image
        image_path = "./tests/test.png"
        image = image_util.load_image(image_path)
        self.assertIsNotNone(image, "Image loading failed, returned None")
        self.assertIsInstance(
            image, pygame.Surface, "Loaded image is not a Pygame Surface instance"
        )


if __name__ == "__main__":
    unittest.main()
