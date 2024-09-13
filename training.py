import pandas as pd
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# Load the dataset
train_df = pd.read_csv('dataset/train.csv')

# Assuming images have been downloaded to a local directory
image_dir = 'images/'  # Path to your downloaded images

# Split the data into training and validation sets
train_data, val_data = train_test_split(train_df, test_size=0.2, random_state=42)

# Data generators for loading and augmenting images
train_datagen = ImageDataGenerator(
    rescale=1./255,        # Normalize pixel values
    rotation_range=20,     # Data augmentation
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_dataframe(
    train_data,
    directory=image_dir,
    x_col='image_link',  # Assuming images are downloaded locally
    y_col='entity_name', # Labels (e.g., 'item_weight', 'voltage')
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'  # Use categorical for multi-class classification
)

val_generator = val_datagen.flow_from_dataframe(
    val_data,
    directory=image_dir,
    x_col='image_link',
    y_col='entity_name',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
