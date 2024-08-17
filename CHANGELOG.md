
# Changelog

## [0.2.0] - 2024-08-17

### Changed
- **Updated `numeric_sort_key`**: Enhanced the key function used for sorting filenames. The function now handles filenames with both numeric and non-numeric parts more effectively, ensuring correct numerical sorting.

### Added
- **`load_state_frames` Function**: Introduced a new function to load images from subdirectories. This function scales images based on the provided ratio or size and organizes them by subdirectory.
- **`load_frames` Function**: Added a function to load and scale images from a single directory, with support for optional scaling by ratio or size.

### Fixed
- **Sorting Behavior**: Improved the sorting algorithm to handle filenames with mixed numeric and non-numeric content correctly.

### Notes
- Make sure to update your `pygame_utility` package to the latest version to benefit from these improvements.


## [0.1.1] - 2024-07-23
### Added
- `__init__.py` now imports `load_image`, `load_state_frames`, and `load_frames` for easier access.
- Correct type hinting in `image_util.py`
- Add documentation

