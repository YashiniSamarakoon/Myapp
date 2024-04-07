from PIL import Image
import numpy as np
from collections import Counter
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder

def predict_labels(image_paths, model_path, actual_labels=None, target_size=(224, 224)):
    # Load the trained model
    model = load_model(model_path)

    # Preprocess images
    def preprocess_image(image_path, target_size):
        image = Image.open(image_path)
        image = image.resize(target_size)
        image = np.array(image) / 255.0  # Normalize pixel values
        return image

    # Preprocess test images
    test_images = [preprocess_image(image_path, target_size) for image_path in image_paths]

    # Convert list of images to numpy array
    test_images = np.array(test_images)

    # Perform predictions
    predictions = model.predict(test_images)

    # Get predicted labels
    predicted_labels = np.argmax(predictions, axis=1)

    # Count the occurrences of each predicted label
    predicted_label_counts = Counter(predicted_labels)

    # Total number of predictions
    total_predictions = len(predicted_labels)
    print("Total predictions:", total_predictions)

    # Calculate the percentage of each predicted class
    class_percentages = {label: count / total_predictions * 100 for label, count in predicted_label_counts.items()}

    # Load the label encoder
    label_encoder = LabelEncoder()

    # If actual labels are provided, encode them and calculate their counts
    if actual_labels:
        actual_labels_encoded = label_encoder.fit_transform(actual_labels)
        actual_label_counts = Counter(actual_labels_encoded)
        # print("\nActual Label Counts:")
        # for label, count in actual_label_counts.items():
        #     print(f"Actual Label: {label}, Count: {count}")

    # Print the count and percentage of each predicted class along with the class name
    print("\nPredicted Label Counts:")
    for label, percentage in class_percentages.items():
        class_name = label_encoder.inverse_transform([label])[0]
        print(f"Predicted Label: {label} ({class_name}), Percentage: {percentage:.2f}%, Count: {predicted_label_counts[label]}")

# Example usage:

# List of image paths
image_paths = [
    'C:\\FYP\\foam1.png',
    'C:\\FYP\\foam2.png',
    'C:\\FYP\\foam3.jpg',
    'C:\\FYP\\glass1.jpg',
    'C:\\FYP\\glass2.jpg',
    'C:\\FYP\\glass3.jpg',
    'C:\\FYP\\metal1.jpg'
    # Add more image paths here as needed
]

# Actual labels corresponding to the images (if available)
actual_labels = ['plastic', 'plastic', 'metal', 'metal', 'glass', 'glass', 'foam', 'foam']

# Path to the trained model
model_path = 'model1.h5'

# Call the function to predict labels and print percentages
predict_labels(image_paths, model_path, actual_labels)