# pull base image
FROM python:3

# path to the working directory
ARG IMAGE_PATH=/opt/restaurant/src

# set environment variables
ENV PYTHONBUFFERED=1
ENV CONFIG_PATH=$IMAGE_PATH/example_restaurant.conf

# set workdir
WORKDIR $IMAGE_PATH

# install dependencies
RUN pip install --upgrade pip
COPY REQUIREMENTS.txt $IMAGE_PATH
RUN pip install -r REQUIREMENTS.txt

# copy project files
COPY restaurant $IMAGE_PATH
COPY example_restaurant.conf $IMAGE_PATH

CMD python manage.py test
