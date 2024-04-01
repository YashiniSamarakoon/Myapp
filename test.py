
import pandas as pd
from PIL import Image
import numpy as np
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from keras.models import Sequential
from keras.models import load_model
from sklearn.metrics import accuracy_score, classification_report

# Load CSV containing test image paths and labels
test_csv_path = 'C:\\FYP\\test_dataset.csv'
test_df = pd.read_csv(test_csv_path)

# Define label encoding for the four labels
label_encoder = LabelEncoder()
label_encoder.fit(['Metal', 'Foam', 'Plastic', 'Glass'])

# Transform the labels in the test dataset
test_df['label'] = label_encoder.transform(test_df['label'])

# Preprocess test images
def preprocess_image(image_path, target_size):
    image = Image.open(image_path)
    image = image.resize(target_size)
    image = np.array(image) / 255.0  # Normalize pixel values
    return image

test_images = [preprocess_image(image_path, (224, 224)) for image_path in test_df['image_path']]
test_labels = test_df['label'].values

# Convert list of images to numpy array
test_images = np.array(test_images)


# Load the Keras model
model = load_model('model1.h5')
predictions = model.predict(test_images)

# Convert predictions to class labels
predicted_labels = label_encoder.inverse_transform(np.argmax(predictions, axis=1))

# Print actual and predicted waste types
for image_path, actual_label, predicted_label in zip(test_df['image_path'], label_encoder.inverse_transform(test_df['label']), predicted_labels):
    print(f"Image: {image_path}, Actual Label: {actual_label}, Predicted Label: {predicted_label}")

# Count the occurrences of each predicted label
predicted_label_counts = Counter(predicted_labels)

# Total number of predictions
total_predictions = len(predicted_labels)
print("Total predictions:", total_predictions)

# Calculate the percentage of each class
class_percentages = {label: (count, count / total_predictions * 100) for label, count in predicted_label_counts.items()}

# Print the percentage of each class
for label, percentage in class_percentages.items():
    print(f"{label}: {percentage:.2f}%")


# Print the count and percentage of each class
#for label, (count, percentage) in class_percentages.items():
#    print(f"{label}: Count: {count}, Percentage: {percentage:.2f}%")
