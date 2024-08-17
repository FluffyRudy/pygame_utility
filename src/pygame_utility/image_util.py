import pygame
from pathlib import Path
from typing import Optional, Union, Tuple, List
from utils.sortkeys import get_numeric_sort_key


def load_image(
    path: Union[str, Path],
    scale_ratio: Tuple[float, float] = (1.0, 1.0),
    scale_size: Optional[Tuple[int, int]] = None,
) -> Optional[pygame.Surface]:
    """
    Load an image from the given path and return it as a pygame Surface, scaled by the given ratio or size.

    Args:
        path (Union[str, Path]): Path of the image file.
        scale_ratio (Tuple[float, float]): Tuple representing the scaling ratio for width and height. Defaults to (1.0, 1.0).
        scale_size (Optional[Tuple[int, int]]): Tuple representing the target width and height in pixels.
            If provided, `scale_size` takes priority over `scale_ratio`.

    Returns:
        Optional[pygame.Surface]: The loaded and scaled image as a pygame Surface object, or None if loading fails.
    """
    image = None
    try:
        image = pygame.image.load(str(path)).convert_alpha()
        if scale_size:
            image = pygame.transform.scale(image, scale_size)
        elif scale_ratio != (1.0, 1.0):
            image = pygame.transform.scale_by(image, scale_ratio)
    except Exception as error:
        print(error)
    finally:
        return image


def load_state_frames(
    path: Union[str, Path],
    scale_ratio: Tuple[float, float] = (1.0, 1.0),
    scale_size: Optional[Tuple[int, int]] = None,
) -> dict[str, List[Optional[pygame.Surface]]]:
    """
    Load multiple frames (images) from subdirectories of the given path and return them as a dictionary of Lists of pygame Surfaces.
    The images within each subdirectory are loaded in alphabetical order.

    Args:
        path (Union[str, Path]): Path of the directory containing subdirectories of image files.
        scale_ratio (Tuple[float, float]): Tuple representing the scaling ratio for width and height. Defaults to (1.0, 1.0).
        scale_size (Optional[Tuple[int, int]]): Tuple representing the target width and height in pixels.
            If provided, `scale_size` takes priority over `scale_ratio`.

    Returns:
        dict[str, List[Optional[pygame.Surface]]]: A dictionary where keys are subdirectory names and values are Lists of loaded and scaled frames as pygame Surface objects.
    """
    frames = {}

    if not Path(path).exists():
        return frames

    for subdir in sorted(Path(path).iterdir(), key=get_numeric_sort_key):
        if subdir.is_dir():
            frame_name = subdir.name
            frames[frame_name] = []
            for file in sorted(subdir.iterdir()):
                if file.suffix != ".png":
                    print(f"WARNING: {file.name} is not a .png file")
                    continue
                surface = load_image(file, scale_ratio, scale_size)
                frames[frame_name].append(surface)

    return frames


def load_frames(
    path: Union[str, Path],
    scale_ratio: Tuple[float, float] = (1.0, 1.0),
    scale_size: Optional[Tuple[int, int]] = None,
) -> List[Optional[pygame.Surface]]:
    """
    Load frames (images) from the given path and return them as a List of pygame Surfaces.
    The images within the directory are loaded in alphabetical order.

    Args:
        path (Union[str, Path]): Path of the directory containing image files.
        scale_ratio (Tuple[float, float]): Tuple representing the scaling ratio for width and height. Defaults to (1.0, 1.0).
        scale_size (Optional[Tuple[int, int]]): Tuple representing the target width and height in pixels.
            If provided, `scale_size` takes priority over `scale_ratio`.

    Returns:
        List[Optional[pygame.Surface]]: A List of loaded and scaled frames as pygame Surface objects.
    """
    frames = []

    if not Path(path).exists():
        return frames

    for file in sorted(Path(path).iterdir(), key=get_numeric_sort_key):
        if file.suffix != ".png":
            print(f"WARNING: {file.name} is not a .png file")
            continue
        surface = load_image(file, scale_ratio, scale_size)
        frames.append(surface)

    return frames
