from setuptools import setup, find_packages

setup(
    name='image_transformer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.4',
        'opencv-python==4.3.0.38',
    ],
    extras_require={
        'dev': [
            'pytest',
            'black==23.7.0',
            'flake8==6.1.0',
        ],
    },
    test_requires=[
        'pytest',
    ],
    author='Tilly Worlidge',
    author_email='matilda.worlidge@gmail.com',
    description='A Python package for sampling non-overlapping regions from an image.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/mworlidge/image-transformer.git",
)
