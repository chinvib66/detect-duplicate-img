# Remove Duplicate Images

A simple CLI tool for detecting and removing duplicate images from a dataset.

The tool uses **image hashing**, specifically 'Difference Hashing' to identify the duplicates in folder.

## Usage

```
> git clone https://github.com/chinvib66/detect-duplicate-img.git
> cd detect-duplicate-img
> pipenv install
> pipenv shell
> python .\cli.py --dataset \path\to\img\dataset --remove 0
```

- --dataset: Absolute path to your dataset folder
- --remove: To permenantly remove the duplicates, set to 1; just to detect with out removing, set to 0

## Concept

Steps:

1. Convert Image to grayscale
2. Resize to 9x8 (to create near 64 bit hash)
3. Compute difference between adjacent pixels
4. Build Hash by comparing adjacent pixels

Tutorial referred:

1. [Image Hashing](https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/)
2. [Detect Duplicates](https://www.pyimagesearch.com/2020/04/20/detect-and-remove-duplicate-images-from-a-dataset-for-deep-learning/?__s=jf8lcs6zi9dzc7dq1mbe)
