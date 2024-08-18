from typing import Union, Tuple
from pathlib import Path
import re


def get_numeric_sort_key(filepath: Union[Path, str]) -> Tuple[float, str]:
    """
    Extract the numeric part from a file path for sorting. If no numeric part is found, return infinity.

    Args:
        filepath (Union[Path, str]): The file path to extract the numeric part from. Can be a Path object or a string.

    Returns:
        Tuple[float, str]: A tuple containing the numeric part as a float (or infinity if no number is found)
                            and the original file path. The tuple is used for sorting files primarily by
                            the numeric part and secondarily by the file path if needed.

    Example without callback:
        >>> files = ['file10.txt', 'file2.txt', 'file1.txt']
        >>> sorted(files)
        ['file1.txt', 'file10.txt', 'file2.txt']

    Example with `get_numeric_sort_key` callback:
        >>> files = ['file10.txt', 'file2.txt', 'file1.txt']
        >>> sorted(files, key=get_numeric_sort_key)
        ['file1.txt', 'file2.txt', 'file10.txt']

    Example with no numeric part:
        >>> files = ['fileA.txt', 'fileB.txt', 'file.txt']
        >>> sorted(files, key=get_numeric_sort_key)
        ['file.txt', 'fileA.txt', 'fileB.txt']
    """
    if isinstance(filepath, Path):
        filepath = str(filepath)

    match = re.search(r"\d+", filepath)
    number = int(match.group()) if match else float("inf")

    return (number, filepath)
