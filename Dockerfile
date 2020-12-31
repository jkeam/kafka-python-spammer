FROM registry.redhat.io/ubi8/python-36

WORKDIR /usr/local/app
COPY . .

RUN pip3 install -r ./requirements.txt

USER nobody
CMD ["python3", "./app.py"]
