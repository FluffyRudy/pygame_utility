import pygame
from pathlib import Path
from typing import Optional, Union, Tuple, List


def load_image(
    path: Union[str, Path],
    scale_ratio: Optional[Tuple[float, float]] = (1.0, 1.0),
    scale_size: Optional[Tuple[float, float]] = None,
) -> Optional[pygame.Surface]:
    """
    Load an image from the given path and return it as a pygame Surface, scaled by the given ratio or size.

    Args:
        path (str): Path of the image file.
        scale_ratio (Optional[Tuple[float, float]]): Tuple representing the scaling ratio for width and height. Takes priority over scale_size if provided.
        scale_size (Optional[Tuple[float, float]]): Tuple representing the target width and height in pixels. Used if scale_ratio is None.

    Returns:
        pygame.Surface: The loaded and scaled image as a pygame Surface object.
    """
    image = None
    try:
        image = pygame.image.load(str(path)).convert_alpha()
        if scale_ratio:
            image = pygame.transform.scale_by(image, scale_ratio)
        elif scale_size:
            image = pygame.transform.scale(image, scale_size)
    except Exception as error:
        print(error)
    finally:
        return image


def load_state_frames(
    path: Union[str, Path],
    scale_ratio: Optional[Tuple[float, float]] = (1.0, 1.0),
    scale_size: Optional[Tuple[float, float]] = None,
) -> dict[str, List[pygame.Surface]]:
    """
    Load multiple frames (images) from subdirectories of the given path and return them as a dictionary of Lists of pygame Surfaces.

    Args:
        path (str): Path of the directory containing subdirectories of image files.
        scale_ratio (Optional[Tuple[float, float]]): Tuple representing the scaling ratio for width and height. Takes priority over scale_size if provided.
        scale_size (Optional[Tuple[float, float]]): Tuple representing the target width and height in pixels. Used if scale_ratio is None.

    Returns:
        dict[str, List[pygame.Surface]]: A dictionary where keys are subdirectory names and values are Lists of loaded and scaled frames as pygame Surface objects.
    """
    frames = {}

    if not Path(path).exists():
        return frames

    for subdir in sorted(Path(path).iterdir()):
        frame_name = subdir.name
        frames[frame_name] = []
        for file in subdir.iterdir():
            if file.suffix == ".png":
                surface = load_image(Path(path) / file, scale_ratio, scale_size)
                frames[frame_name].append(surface)

    return frames


def load_frames(
    path: Union[str, Path],
    scale_ratio: Optional[Tuple[float, float]] = (1.0, 1.0),
    scale_size: Optional[Tuple[float, float]] = None,
) -> List[pygame.Surface]:
    """
    Load frames (images) from the given path and return them as a List of pygame Surfaces.

    Args:
        path (str): Path of the directory containing image files.
        scale_ratio (Optional[Tuple[float, float]]): Tuple representing the scaling ratio for width and height. Takes priority over scale_size if provided.
        scale_size (Optional[Tuple[float, float]]): Tuple representing the target width and height in pixels. Used if scale_ratio is None.

    Returns:
        List[pygame.Surface]: A List of loaded and scaled frames as pygame Surface objects.
    """
    frames = []

    if not Path(path).exists():
        return frames

    for file in sorted(Path(path).iterdir()):
        image_path: Path = Path(path) / file
        if not file.suffix == ".png":
            print(f"WARNING: {image_path.name} is not .png file")
            continue
        surface = load_image(image_path, scale_ratio, scale_size)
        frames.append(surface)

    return frames
