# Copyright 2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import tensorflow as tf

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
