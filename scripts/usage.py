from image_transformer.transformer import ImageTransformer


# Path to your input image
image_path = "path/to/image.jpg"

# Instantiate the sampler with the image path
sampler = ImageTransformer(image_path)

# Define the sample size (width, height)
sample_width = 100
sample_height = 100

# Number of samples to generate
num_samples = 3

# Get the random non-overlapping samples
samples = sampler.get_random_samples(sample_width, sample_height, num_samples)

# Define output paths for the samples
output_paths = ["sample1.jpg", "sample2.jpg", "sample3.jpg"]

# Save the samples to disk
sampler.save_samples(samples)

print("Samples saved to:", output_paths)
