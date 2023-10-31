
# Run this file using Streamlit command: streamlit run main.py

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io

class CoffeeLandClassifier:
    def __init__(self, model_path, class_labels):
        self.model = tf.keras.models.load_model(model_path)
        self.class_labels = class_labels

    def run(self):
        st.title("Coffee Land Classifier")

        # Create a file uploader widget
        uploaded_image = st.file_uploader("Please upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            # Load and preprocess the uploaded image
            img = Image.open(uploaded_image)
            img = img.resize((64, 64))  # Resize the image to match the model's input shape
            img = np.array(img)
            img = img.astype('float32') / 255.0
            img = np.expand_dims(img, axis=0)

            # Make a prediction
            predictions = self.model.predict(img)
            class_index = np.argmax(predictions)
            predicted_class = self.class_labels[class_index]

            # Display the uploaded image
            st.image(img[0])

            # Show the prediction result
            st.write(f"Prediction: {predicted_class}")
            st.write("Class Probabilities:")
            for i, prob in enumerate(predictions[0]):
                st.write(f"{self.class_labels[i]}: {prob * 100:.2f}%")

def main():
    model_path = "model.h5"
    class_labels = ["Coffee Land", "Not Coffee Land"]  # Class labels
    classifier = CoffeeLandClassifier(model_path, class_labels)
    classifier.run()

if __name__ == "__main__":
    main()
