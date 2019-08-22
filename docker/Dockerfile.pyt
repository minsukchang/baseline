FROM pytorch/pytorch:latest
FROM python:3.6 
RUN apt-get update && \
    apt-get install -y apt-utils g++ make git vim cython && \
    pip install --upgrade pip && \
    pip install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp36-cp36m-linux_x86_64.whl && \
    pip install torchvision && \
    pip install visdom pymongo pyyaml jupyter && \
    jupyter nbextension enable --py widgetsnbextension

COPY python /baseline/python
COPY docs /baseline/docs

RUN  cd /baseline/python/ && bash ./install_dev.sh baseline no_test

ADD https://github.com/mead-ml/xpctl/archive/master.tar.gz ./xpctl-master.tar.gz
RUN tar xzf xpctl-master.tar.gz && \
    cd ./xpctl-master/ && \
    pip install -e .

ADD https://github.com/mead-ml/hpctl/archive/master.tar.gz ./hpctl-master.tar.gz
RUN tar xzf hpctl-master.tar.gz && \
    cd ./hpctl-master/ && \
    pip install -e .

VOLUME ["/data/embeddings", "/data/model-store", "/data/datasets", "/data/model-checkpoints"]

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /baseline/python
CMD ["bash"]
