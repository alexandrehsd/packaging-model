FROM python:3.8

# Copy the requirements file
COPY ./requirements.txt /webapp/requirements.txt

# Install dependencies
RUN pip install -r /webapp/requirements.txt

# Set /webapp as the current working directory
WORKDIR /webapp

# Copy the ONNX model to a separate directory (if it's a model)
COPY webapp/models/roberta-sequence-classification-9.onnx /webapp/models/

# Copy local content of webapp into the container
COPY webapp/app.py /webapp/app.py

ENTRYPOINT ["python"]

CMD ["app.py"]