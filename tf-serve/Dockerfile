FROM tensorflow/serving

MAINTAINER "Rabii Elbeji"

LABEL version="1.0.0"
LABEL description="First version of the model"

RUN apt-get clean

RUN mkdir serving

ADD ./models /models
ADD ./config/model_config /serving/model_config

EXPOSE 8500
EXPOSE 8501

ENTRYPOINT ["tensorflow_model_server", "--model_config_file=/serving/model_config", "--port=8500", "--rest_api_port=8501"]
