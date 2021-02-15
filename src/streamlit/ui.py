# Copyright 2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import streamlit as st

import requests

from utils import image2tensor
from constants import REST_URL, MAPPING

# General information about the UI
st.title("TensorFlow Serving + Streamlit! :sparkles: :framed_picture:")
st.header("UI to use a TensorFlow image classification model of The Simpsons characters (named SimpsonsNet) served with TensorFlow Serving.")

# Show which are the classes that the SimpsonsNet model can predict
if st.checkbox("Show classes"):
    st.write(f"The SimpsonsNet can predict the following characters: {MAPPING}")

# Create a FileUploader so that the user can upload an image to the UI
uploaded_file = st.file_uploader(label="Upload an image of any of the available The Simpsons characters (please see Classes).",
                                 type=["png", "jpeg", "jpg"])

# Display the predict button just when an image is being uploaded
if not uploaded_file:
    st.warning("Please upload an image before proceeding!")
    st.stop()
else:
    image_as_bytes = uploaded_file.read()
    st.image(image_as_bytes, use_column_width=True)
    pred_button = st.button("Predict")

if pred_button:
    # Converts the input image into a Tensor
    image_tensor = image2tensor(image_as_bytes=image_as_bytes)

    # Prepare the data that is going to be sent in the POST request
    json_data = {
        "instances": image_tensor
    }

    # Send the request to the Prediction API
    response = requests.post(REST_URL, json=json_data)

    # Retrieve the highest probablity index of the Tensor (actual prediction)
    prediction = response.json()['predictions'][0]
    label = prediction2label(prediction=prediction)

    # Write the predicted label for the input image
    st.write(f"Predicted The Simpsons character is: {label}")