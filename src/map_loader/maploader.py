from typing import Union, Optional, List, Tuple, Dict
from pytmx import load_pygame
from pytmx import TiledTileLayer, TiledObjectGroup, TiledImageLayer
from pytmx.pytmx import TiledGroupLayer
from pygame import Surface
from pathlib import Path


class MapLoaderError(Exception):
    """Custom exception for MapLoader errors."""

    def __init__(self, message: str):
        """
        Initialize the exception with a message.

        Args:
            message (str): Error message.
        """
        super().__init__(message)


class MapLoader:
    """Class for loading and managing TMX maps."""

    def __init__(self, filepath: Union[str, Path]):
        """
        Initialize the MapLoader with a TMX file.

        Args:
            filepath (Union[str, Path]): Path to the .tmx file.

        Raises:
            FileNotFoundError: If the file does not exist.
            MapLoaderError: If the file is not a .tmx file.
        """
        path = Path(filepath)
        if not path.exists():
            message = f"File not found at {path.absolute()}"
            raise FileNotFoundError(message)
        elif path.suffix != ".tmx":
            message = f"Invalid file type: {path.suffix}. Expected a .tmx file."
            raise MapLoaderError(message)

        self.__map_data = load_pygame(str(filepath))
        self.map_props = {
            "tile_size": (self.__map_data.tilewidth, self.__map_data.tileheight),
            "tile_counts": (self.__map_data.width, self.__map_data.height),
        }

    @property
    def all_layernames(self) -> List[str]:
        """
        Get all layer names except TiledGroupLayer.

        Returns:
            List[str]: List of layer names.
        """
        layernames = list(self.__map_data.layernames.keys())
        filtered_layers = []
        for layername in layernames:
            layer = self.__map_data.get_layer_by_name(layername)
            if not isinstance(layer, TiledGroupLayer):
                filtered_layers.append(layername)
        return filtered_layers

    def get_layer_data_by_name(
        self, name: str, only_coord: bool
    ) -> List[Tuple[int, int, Optional[Surface]]]:
        """
        Get data for a specific layer by name.

        Args:
            name (str): Name of the layer.
            only_coord (bool): If True, return only coordinates; otherwise, include images.

        Returns:
            List[Tuple[int, int, Optional[Surface]]]: List of tuples containing x, y, and the image (or None).

        Raises:
            ValueError: If the layer does not exist.
        """
        try:
            layer = self.__map_data.get_layer_by_name(name)
        except ValueError:
            message = f"Layer {name} doesn't exist"
            raise ValueError(message)

        if isinstance(layer, TiledTileLayer):
            return self.__get_tile_layer_data(layer, only_coord)
        elif isinstance(layer, TiledObjectGroup):
            return self.__get_tiled_object_layer(layer, only_coord)
        elif isinstance(layer, TiledImageLayer):
            return [(0, 0, layer.image)]

        return []

    def get_map_data(self) -> Dict[str, List[Tuple[int, int, Optional[Surface]]]]:
        """
        Get data for all layers in the map.

        Returns:
            Dict[str, List[Tuple[int, int, Optional[Surface]]]]: Dictionary with layer names as keys and layer data as values.
        """
        data = {}
        for layername in self.all_layernames:
            data[layername] = self.get_layer_data_by_name(layername, only_coord=False)
        return data

    def ok(self) -> None:
        """Clean up map data."""
        del self.map_data

    def __get_tile_layer_data(
        self, layer: TiledTileLayer, only_coord: bool
    ) -> List[Tuple[int, int, Optional[Surface]]]:
        """
        Get data for a TiledTileLayer.

        Args:
            layer (TiledTileLayer): The tile layer.
            only_coord (bool): If True, return only coordinates; otherwise, include images.

        Returns:
            List[Tuple[int, int, Optional[Surface]]]: List of tuples containing x, y, and the image (or None).
        """
        layer_data = []
        w, h = self.map_props["tile_size"]
        for tile_data in layer:
            x, y, gid = tile_data
            surface = self.__get_image_by_gid(gid)
            if only_coord:
                layer_data.append((x * w, y * h, None))
            elif surface is not None:
                layer_data.append((x * w, y * h, surface))
        return layer_data

    def __get_tiled_object_layer(
        self, layer: TiledObjectGroup, only_coord: bool
    ) -> List[Tuple[int, int, Optional[Surface]]]:
        """
        Get data for a TiledObjectGroup.

        Args:
            layer (TiledObjectGroup): The object group layer.
            only_coord (bool): If True, return only coordinates; otherwise, include images.

        Returns:
            List[Tuple[int, int, Optional[Surface]]]: List of tuples containing x, y, and the image (or None).
        """
        layer_data = []
        for data in layer:
            x, y, surface = data.x, data.y, data.image
            if only_coord:
                layer_data.append((x, y, None))
            else:
                layer_data.append((x, y, surface))
        return layer_data

    def __get_image_by_gid(self, gid: int) -> Optional[Surface]:
        """
        Get an image by its GID.

        Args:
            gid (int): The global ID of the tile.

        Returns:
            Optional[Surface]: The image associated with the GID, or None if not found.
        """
        image = None
        try:
            image = self.__map_data.get_tile_image_by_gid(gid)
        except TypeError:
            print("GID must be an integer.")
        except ValueError:
            pass  # Return None if the image for the GID doesn't exist
        return image
