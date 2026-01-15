# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 15:32:20 2025

@author: Sianna.Groesser
"""

import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
import os

# ======================
# Parameters
# ======================
N_IMAGES = 29
IMG_SIZE = 256          # square size (e.g. 256x256)
OUT_DIR = r"C:\sync_folder\TSRlearn-task\stimuli\mask_images"

np.random.seed(None)

os.makedirs(OUT_DIR, exist_ok=True)

# ======================
# Mask generators
# ======================
def binary_noise_mask(size, p=0.5):
    """
    High-frequency binary noise (salt-and-pepper),
    matching the reference image.
    """
    mask = (np.random.rand(size, size) < p).astype(np.uint8) * 255
    return mask

def gray_mask(size, level=128):
    return np.full((size, size), level, dtype=np.uint8)

def clustered_binary_noise_mask(size, sigma=0.5):
    noise = np.random.rand(size, size)
    smooth = gaussian_filter(noise, sigma=sigma)
    binary = (smooth > np.median(smooth)).astype(np.uint8) * 255
    return binary

def clustered_rgb_noise_mask(size, sigma=0.5):
    # Random noise per channel
    noise = np.random.rand(size, size, 3)

    # Smooth each channel independently
    smooth = np.zeros_like(noise)
    for c in range(3):
        smooth[..., c] = gaussian_filter(noise[..., c], sigma=sigma)

    # Normalize to [0, 255]
    smooth -= smooth.min()
    smooth /= smooth.max()
    rgb = (smooth * 255).astype(np.uint8)

    return rgb

images = []

n_gray = 0
n_rgb_noise = 29  # main reference-like masks

for _ in range(n_gray):
    images.append(gray_mask(IMG_SIZE))

for _ in range(n_rgb_noise):
    images.append(clustered_rgb_noise_mask(IMG_SIZE))

np.random.shuffle(images)
images = images[:N_IMAGES]

# ======================
# Save
# ======================
for i, img in enumerate(images):
    Image.fromarray(img).save(
        os.path.join(OUT_DIR, f"mask_{i:02d}.png")
    )

