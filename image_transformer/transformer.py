import cv2
import random
import numpy as np
from typing import List, Tuple


class ImageTransformer:
    def __init__(self, image_path: str):
        """
        Initialize the ImageTransformer with an image path.

        Args:
            image_path (str): The path of the image from which to sample.

        Raises:
            ValueError: If the image cannot be loaded from the specified path.
        """
        self.image = cv2.imread(image_path)

        if self.image is None:
            raise ValueError(f"Unable to load image from {image_path}")

        # Store image dimensions
        self.height, self.width = self.image.shape[:2]

    def validate_sample_size(self, sample_width: int, sample_height: int):
        """
        Checks if the sample size is valid for the given image dimensions.

        Args:
            sample_width (int): Width of the sample.
            sample_height (int): Height of the sample.

        Raises:
            ValueError: If the sample size is not positive or
                is larger than the image dimensions.
        """
        if sample_width <= 0 or sample_height <= 0:
            raise ValueError("Sample size must be positive.")
        if sample_width > self.width or sample_height > self.height:
            raise ValueError("Sample size must be smaller than the image dimensions.")

    @staticmethod
    def _is_overlapping(
        sample1: Tuple[int, int, int, int], sample2: Tuple[int, int, int, int]
    ):
        """Internal function to check if two samples overlap.

        Args:
            sample1 (Tuple[int, int, int, int]):
                Coordinates of the first sample (left, top, right, bottom).
            sample2 (Tuple[int, int, int, int]):
                Coordinates of the second sample (left, top, right, bottom).

        Returns:
            bool: True if the rectangles overlap, otherwise False.
        """
        left1, top1, right1, bottom1 = sample1
        left2, top2, right2, bottom2 = sample2
        return not (
            right1 <= left2 or right2 <= left1 or bottom1 <= top2 or bottom2 <= top1
        )

    def get_random_samples(
        self, sample_width: int, sample_height: int, num_samples: int = 3
    ):
        """
        Generates random non-overlapping samples from the image.

        Args:
            sample_width (int): Width of each sample.
            sample_height (int): Height of each sample.
            num_samples (int): Number of samples to generate.
                Defaults to 3.

        Returns:
            List[np.ndarray]: A list of numpy.ndarray objects representing the samples.

        Raises:
            RuntimeError: If the specified number of non-overlapping samples cannot be generated.
        """
        # Validate sample size
        self.validate_sample_size(sample_width, sample_height)

        samples = []
        attempts = 0
        max_attempts = 1000

        while len(samples) < num_samples and attempts < max_attempts:
            attempts += 1
            left = random.randint(0, self.width - sample_width)
            top = random.randint(0, self.height - sample_height)
            sample = (left, top, left + sample_width, top + sample_height)

            if not any(self._is_overlapping(sample, s) for s in samples):
                samples.append(sample)

        if len(samples) < num_samples:
            raise RuntimeError("Unable to generate non-overlapping samples.")

        return [
            self.image[top:bottom, left:right] for (left, top, right, bottom) in samples
        ]

    def save_samples(self, samples: List[np.ndarray], output_paths: List[str] = None):
        """
        Saves the samples to specified file paths.

        Args:
            samples (list): A list of numpy.ndarray objects representing the samples.
            output_paths (list): A list of file paths to save the samples.

        Raises:
            ValueError: If the number of samples and output paths are not equal.
        """
        if output_paths is None:
            output_paths = [f'sample_{i}.jpg' for i in range(len(samples))]
        if len(samples) != len(output_paths):
            raise ValueError("Number of samples and output paths must be equal.")
        for sample, path in zip(samples, output_paths):
            cv2.imwrite(path, sample)
