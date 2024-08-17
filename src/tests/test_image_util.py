# tests/test_image_util.py

import unittest
import pygame
from src.pygame_utility import image_util
from src.utils.sortkeys import get_numeric_sort_key


class TestImageUtil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        display_mode = pygame.display.set_mode((0, 0))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_load_image(self):
        image_path = "src/tests/test.png"
        image = image_util.load_image(image_path)
        self.assertIsNotNone(image, "Image loading failed, returned None")
        self.assertIsInstance(
            image, pygame.Surface, "Loaded image is not a Pygame Surface instance"
        )

    def test_load_frames(self):
        image_path = "./tests/"
        frames = image_util.load_frames(image_path)
        self.assertIsInstance(frames, list, "loaded container is not a list")

        for frame in frames:
            self.assertIsInstance(
                frame, pygame.Surface, "Each frame should be instance of pygame.Surface"
            )


class TestSortKeys(unittest.TestCase):
    def test_numeric_sort_key(self):
        files = [
            "file01.png",
            "file1.png",
            "file100.png",
            "file2.png",
        ]
        sorted_files = sorted(files, key=get_numeric_sort_key)
        self.assertEqual(
            sorted_files, ["file01.png", "file1.png", "file2.png", "file100.png"]
        )

    def test_non_numeric_files(self):
        files = ["fileA.png", "fileB.png", "fileC.png"]
        sorted_files = sorted(files, key=get_numeric_sort_key)
        self.assertEqual(sorted_files, files)

    def test_mixed_files(self):
        files = ["fileA.png", "file1.png", "fileB.png"]
        sorted_files = sorted(files, key=get_numeric_sort_key)
        self.assertEqual(sorted_files, ["file1.png", "fileA.png", "fileB.png"])


if __name__ == "__main__":
    unittest.main()
