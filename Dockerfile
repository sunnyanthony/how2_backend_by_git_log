FROM python:3

# use apt to install
RUN apt-get update;\
    apt-get install -y netcat

WORKDIR /usr/src/app

# install python module from requirements.txt
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 1234
CMD ["python", "src/socket_example.py"]
