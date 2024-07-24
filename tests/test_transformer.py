import pytest
import cv2
import numpy as np
from image_transformer import ImageTransformer


@pytest.fixture
def setup_image_transformer():
    """Fixture to create a test image and ImageTransformer instance."""
    image_path = 'test_image.jpg'
    dummy_image = np.zeros((1000, 1000, 3), dtype=np.uint8)
    cv2.imwrite(image_path, dummy_image)
    transformer = ImageTransformer(image_path)
    yield transformer

    # Cleanup
    import os
    if os.path.exists(image_path):
        os.remove(image_path)


def test_validate_sample_size_valid(setup_image_transformer):
    """Test for valid sample size."""
    transformer = setup_image_transformer
    transformer.validate_sample_size(100, 100)


def test_validate_sample_size_invalid(setup_image_transformer):
    """Test for invalid sample size (larger than image dimensions)."""
    transformer = setup_image_transformer
    with pytest.raises(ValueError):
        transformer.validate_sample_size(1100, 100)
    with pytest.raises(ValueError):
        transformer.validate_sample_size(100, 1100)
    with pytest.raises(ValueError):
        transformer.validate_sample_size(-100, 100)
    with pytest.raises(ValueError):
        transformer.validate_sample_size(100, -100)


def test_get_random_samples(setup_image_transformer):
    """Test random sample generation."""
    transformer = setup_image_transformer
    samples = transformer.get_random_samples(100, 100, num_samples=3)
    assert len(samples) == 3
    for sample in samples:
        assert sample.shape == (100, 100, 3)


def test_save_samples(setup_image_transformer):
    """Test saving samples to files."""
    transformer = setup_image_transformer
    samples = transformer.get_random_samples(100, 100, num_samples=3)
    output_paths = ['sample1.jpg', 'sample2.jpg', 'sample3.jpg']
    transformer.save_samples(samples, output_paths)

    for path in output_paths:
        assert cv2.imread(path) is not None

    # Cleanup
    import os
    for path in output_paths:
        if os.path.exists(path):
            os.remove(path)


def test_get_random_samples_insufficient_attempts(setup_image_transformer):
    """Test handling of failure to generate enough non-overlapping samples."""
    transformer = setup_image_transformer
    # Set a small image size and large sample size to force failure
    transformer.width, transformer.height = 200, 200
    with pytest.raises(RuntimeError):
        transformer.get_random_samples(150, 150, num_samples=10)
