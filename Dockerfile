FROM python:3.10.6

# copy requirements into image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install the dependencies
RUN pip install -r requirements.txt

# copy files to image
COPY . /app

ENTRYPOINT [ "python" ]
CMD ["app.py" ]
