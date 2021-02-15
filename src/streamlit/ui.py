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


# def process(image, server_url: str):

#     m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

#     r = requests.post(
#         server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
#     )

#     return r


# # construct UI layout
# st.title("DeepLabV3 image segmentation")

# st.write(
#     """Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
#          This streamlit example uses a FastAPI service as backend.
#          Visit this URL at `:8000/docs` for FastAPI documentation."""
# )  # description and instructions

# input_image = st.file_uploader("insert image")  # image upload widget

# if st.button("Get segmentation map"):

#     col1, col2 = st.beta_columns(2)

#     if input_image:
#         segments = process(input_image, backend)
#         original_image = Image.open(input_image).convert("RGB")
#         segmented_image = Image.open(io.BytesIO(segments.content)).convert("RGB")
#         col1.header("Original")
#         col1.image(original_image, use_column_width=True)
#         col2.header("Segmented")
#         col2.image(segmented_image, use_column_width=True)

#     else:
#         # handle case with no image
#         st.write("Insert an image!")