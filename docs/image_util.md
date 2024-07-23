# image_util Module

The `image_util` module provides functions for easier loading images in Pygame from directory as list of frames of state based frames.

## Functions

### `load_image`

```python
load_image(
    path: Union[str, Path],
    scale_ratio: Tuple[float, float] = (1.0, 1.0),
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
```

```python
load_state_frames(
    path: Union[str, Path],
    scale_ratio: Tuple[float, float] = (1.0, 1.0),
    scale_size: Optional[Tuple[float, float]] = None,
) -> dict[str, List[pygame.Surface]]:
    """
    Load multiple frames (images) from subdirectories of the given path and return them as a dictionary of Lists of pygame Surfaces.
    The images within each subdirectory are loaded in alphabetical order.

    Args:
        path (str): Path of the directory containing subdirectories of image files.
        scale_ratio (Optional[Tuple[float, float]]): Tuple representing the scaling ratio for width and height. Takes priority over scale_size if provided.
        scale_size (Optional[Tuple[float, float]]): Tuple representing the target width and height in pixels. Used if scale_ratio is None.

    Returns:
        dict[str, List[pygame.Surface]]: A dictionary where keys are subdirectory names and values are Lists of loaded and scaled frames as pygame Surface objects.
    """
```

```python
def load_frames(
    path: Union[str, Path],
    scale_ratio: Tuple[float, float] = (1.0, 1.0),
    scale_size: Optional[Tuple[float, float]] = None,
) -> List[pygame.Surface]:
    """
    Load frames (images) from the given path and return them as a List of pygame Surfaces.
    The images within directory are loaded in alphabetical order.

    Args:
        path (str): Path of the directory containing image files.
        scale_ratio (Optional[Tuple[float, float]]): Tuple representing the scaling ratio for width and height. Takes priority over scale_size if provided.
        scale_size (Optional[Tuple[float, float]]): Tuple representing the target width and height in pixels. Used if scale_ratio is None.

    Returns:
        List[pygame.Surface]: A List of loaded and scaled frames as pygame Surface objects.
    """
```