# Copyright 2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import tensorflow as tf

from constants import MAPPING

def image2tensor(image_as_bytes):
    """
    Receives a image as bytes as input, that will be loaded,
    preprocessed and turned into a Tensor so as to include it
    in the TF-Serving request data.
    """

    # Apply the same preprocessing as during training (resize and rescale)
    image = tf.io.decode_image(image_as_bytes, channels=3)
    image = tf.image.resize(image, [224, 224])
    image = image/255.

    # Convert the Tensor to a batch of Tensors and then to a list
    image = tf.expand_dims(image, 0)
    image = image.numpy().tolist()
    return image


def prediction2label(prediction):
    """
    Receives the prediction Tensor and retrieves the index with the highest
    probability, so as to then map the index value in order to get the
    predicted label. 
    """

    # Retrieve the highest probablity index of the Tensor (actual prediction)
    prediction = tf.argmax(prediction)
    return MAPPING[prediction.numpy()]
