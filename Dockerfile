FROM python:3.8

# copy the requirements file
COPY ./requirements.txt /webapp/requirements.txt

COPY roberta-sequence-classification-9.onnx /webapp

# sets /webapp as current working dir
WORKDIR /webapp

# install dependencies
RUN pip install -r requirements.txt

# copy local content of webapp into the container
COPY webapp/* /webapp

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]