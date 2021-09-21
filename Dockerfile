FROM python:3

ARG IMAGE_PATH=/opt/restaurant/src

ENV PYTHONBUFFERED=1
ENV CONFIG_PATH=$IMAGE_PATH/example_restaurant.conf

WORKDIR $IMAGE_PATH

COPY REQUIREMENTS.txt $IMAGE_PATH

RUN pip install -r REQUIREMENTS.txt

COPY restaurant $IMAGE_PATH

COPY example_restaurant.conf $IMAGE_PATH

RUN python manage.py migrate
