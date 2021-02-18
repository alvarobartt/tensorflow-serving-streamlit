# :framed_picture: Serve TensorFlow ML models with TF-Serving and then create a Streamlit UI to use them!

This is a pretty simple [Streamlit](https://www.streamlit.io/) UI to expose the functionality
of a [TensorFlow](https://www.tensorflow.org/) image classification CNN served using 
[TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving).

In this case, we will be serving the ML model developed at 
[alvarobartt/serving-tensorflow-models](https://github.com/alvarobartt/serving-tensorflow-models), which
is an image classification CNN to classify images from The Simpsons Characters.

---

## :tv: Demo

![](ui-demo.gif)

---

## :whale2: Deployment

In order to deploy the presented application, you will need to use [Docker Compose](https://docs.docker.com/compose/),
which means that you will also need to have [Docker](https://www.docker.com/) installed.

We will deploy the following Docker Containers:

- djfisjfds
- dfsafdsafs

That said, you can easily deploy them with Docker Compose as it follows:

```
docker-compose build --force-rm
```

__Note__: we use `--force-rm` so as to force the removal of the intermediate Docker containers.

Once built, we can proceed to deploy it with the following command:

```
docker-compose up
```

Finally, whenever you want to stop the containers you can use the following command:

```
docker-compose stop
```

And additionally, you can also remove the containers once you don't need them anymore with 
the following command:

```
docker-compose rm
```

---

## :book: Contact information
