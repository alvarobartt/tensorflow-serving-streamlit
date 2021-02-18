# TensorFlow Serving + Streamlit! :sparkles::framed_picture:

__Serve TensorFlow ML models with TF-Serving and then create a Streamlit UI to use them!__

This is a pretty simple [Streamlit](https://www.streamlit.io/) UI to expose the functionality
of a [TensorFlow](https://www.tensorflow.org/) image classification CNN served using 
[TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving).

In this case, we will be serving the ML model developed at 
[alvarobartt/serving-tensorflow-models](https://github.com/alvarobartt/serving-tensorflow-models), which
is an image classification CNN to classify images from 
[The Simpsons Characters](https://www.kaggle.com/alexattia/the-simpsons-characters-dataset).

---

## :tv: Demo

![](ui-demo.gif)

---

## :whale2: Deployment

In order to deploy the presented application, you will need to use [Docker Compose](https://docs.docker.com/compose/),
which means that you will also need to have [Docker](https://www.docker.com/) installed.

We will deploy the following Docker Containers:

- `src/tfserving`: contains the TF-Serving API deployment.
- `src/streamlit`: contains the code of the UI connected to the deployed API.

That said, you can easily deploy them with Docker Compose. So we will start off 
with the initial step which is __building the containers__, with the following command:

```
docker-compose build --force-rm
```

__Note__: we use `--force-rm` so as to force the removal of the intermediate Docker containers.

Once built, we can proceed to __deploy the containers__ with the following command:

```
docker-compose up
```

Finally, whenever you want to __stop the containers__ you can use the following command:

```
docker-compose stop
```

And additionally, you can also __remove the containers__ once you don't need them anymore with 
the following command:

```
docker-compose rm
```

---

## :book: Contact information

You can contact me or know me via any of the following:

- :bird: Twitter: https://twitter.com/alvarobartt
- :octocat: GitHub: https://github.com/alvarobartt
