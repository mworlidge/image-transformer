# Image Transformer

A Python package for sampling non-overlapping regions from an image.

## Installation

To install the package, clone the repository, create and initalise a virutal environment, and install the package using pip:

```bash
git clone https://github.com/mworlidge/image-transformer.git
cd image-transformer
python3 -m venv venv
source venv/bin/activate
pip install .
```

## Usage
Here’s a basic example of how to use the ImageTransformer class:
```
from image_transformer.transformer import ImageTransformer

# Update this with the path to the image you want to sample
image_path = 'path/to/image.jpg'

# Initialize the transformer
transformer = ImageTransformer(image_path)

# Validate sample size
transformer.validate_sample_size(100, 100)

# Get random samples
samples = transformer.get_random_samples(100, 100, num_samples=3)

# Save samples to files
output_paths = ['sample1.jpg', 'sample2.jpg', 'sample3.jpg']
transformer.save_samples(samples, output_paths)
```

This code is in `scripts/usage.py`, you will just need to update the `image_path` variable and then run:
```
python3 scripts/usage.py
```

## Tests
To run tests for the package, use:
```
pytest
```

## Notes

### Current Design:
The ImageTransformer class is responsible for:
- Loading the image.
- Validating sample sizes.
- Checking for overlapping samples.
- Generating non-overlapping random samples.
- Saving samples to disk.

### Improvements:
- Single Responsibility Principle (SRP): Break down responsibilities into separate classes or functions. For example, create separate classes for sampling, validating, and saving if more complex operations are required in the future.
- Transformations: Allow for additional transformations by integrating transformation methods or hooks into the class.

## Extensibility Considerations:
- Subclassing: Subclasses of ImageTransformer could be implemented for different sampling strategies. For example, to add functionality for different kinds of sampling (e.g., grid-based sampling, stratified sampling), new classes could be created that inherit from ImageTransformer and override the methods as needed.
- Additional Transformations:
    - Pre-processing and Post-processing: Methods to preprocess the image before sampling or post-process the samples after extraction. For example, a method to apply image filters or augmentations before sampling could be added.
- Pipeline Integration: The design can be integrated into a larger image processing pipeline where different stages (like transformations, augmentations, or filtering) are chained together.
- Configurability: 
    - Sample Size and Count: Parameters such as sample size and the number of samples are configurable.
    - Overlap Strategies: The current overlap check can be extended to support more complex overlap strategies, like partial overlaps or different spatial constraints.
- Error Handling and Validation:
    - Custom Error Messages: The class can be extended to include more specific error handling and validation rules for different types of input or sampling constraints.
    - Dynamic Checks: Additional checks can be incorporated to handle edge cases or special conditions.
