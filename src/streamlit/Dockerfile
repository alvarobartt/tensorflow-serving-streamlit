# Docker pulls the specified image and sets it as the working image
ARG BASE_IMAGE="ubuntu:20.04"
FROM ${BASE_IMAGE}

# Allow log messages to be dumped in the stream (not buffer)
ENV PYTHONUNBUFFERED TRUE

# Install the Ubuntu dependencies and Python 3
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    ca-certificates \
    python3-dev \
    python3-distutils \
    python3-venv \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && cd /tmp \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && rm get-pip.py

# Create a new Python env and include it in the PATH
RUN python3 -m venv /home/venv
ENV PATH="/home/venv/bin:$PATH"

# Update the default system Python version to Python3/PIP3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN update-alternatives --install /usr/local/bin/pip pip /usr/local/bin/pip3 1

# Creates a new Ubuntu user
RUN useradd -m model-server

# Upgrades PIP before proceeding and installs setuptools
RUN pip install pip --upgrade
RUN pip install -U pip setuptools

# Move the current directory to the Docker image
RUN mkdir /streamlit
COPY . /streamlit
WORKDIR /streamlit

# Install the requirements
RUN pip install -r requirements.txt

# Sets the proper rights to the created Python env
RUN chown -R model-server /home/venv

# Creates a directory for the logs and sets permissions to it
RUN mkdir /home/logs \
    && chown -R model-server /home/logs

# Expose the UI port (8502)
ENV UI_PORT=8502
EXPOSE $UI_PORT

# Prepare the CMD that will be run on docker run
USER model-server
CMD streamlit run ui.py --server.port=$UI_PORT >> /home/logs/ui.log
