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
    img = tf.io.decode_image(image_as_bytes, channels=3)
    img = tf.image.resize(img, [224, 224])
    img = img/255.

    # Convert the Tensor to a batch of Tensors and then to a list
    img = tf.expand_dims(img, 0)
    img = img.numpy().tolist()
    return img
