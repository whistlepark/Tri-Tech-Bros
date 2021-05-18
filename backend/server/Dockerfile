# Python 3.x image
FROM python:3

# Output python to host computer
ENV PYTHONBUFFERED 1

# Define working directory for RUN/CMD/COPY
WORKDIR /app

# copy req's
COPY ./src/requirements.txt /app/

# install req's
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# docker on ports:
EXPOSE 6000

# Start server
CMD ["python", "manage.py"]

