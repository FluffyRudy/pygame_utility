
# Changelog


## [1.1.0] - 2024-08-23

### Added
- **Additional ID in Layer Data**:
  - **`__get_tile_layer_data` and `__get_tiled_object_layer` methods**: Updated these methods to include an additional `int` identifier (`gid` for tile layers and `_id` for object layers) in their return values. The returned tuples now contain `(x, y, surface, id)`.

### Changed
- **Return Type Annotations**:
  - Adjusted the return type annotations for `__get_tile_layer_data`, `__get_tiled_object_layer`, and `get_layer_data_by_name` to reflect the inclusion of the additional identifier.

### Fixed
- **Surface Handling**:
  - Ensured proper handling of `None` values for surfaces when `only_coord` is `True`, maintaining consistent output structure.
