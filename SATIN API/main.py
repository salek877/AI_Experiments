# main.py

from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


app = FastAPI()


class ImageClassifier:
    def __init__(self, model_path):
        self.MODEL = tf.keras.models.load_model(model_path) # Load model
        self.CLASS_NAMES = ["Not Coffee Land", "Coffee Land"]


# Process input data
    def read_file_as_image(self, data) -> np.ndarray:
        image = np.array(Image.open(BytesIO(data)))
        return image

# Return output
    def predict(self, file: UploadFile):
        image = self.read_file_as_image(file.file.read())
        img_batch = np.expand_dims(image, 0)

        predictions = self.MODEL.predict(img_batch)
        predicted_class = self.CLASS_NAMES[np.argmax(predictions[0])]

        return {'class': predicted_class}

classifier = ImageClassifier("model.h5")

# Created this for testing
@app.get("/ping")
async def ping():
    return "Hello World"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    result = classifier.predict(file)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)
